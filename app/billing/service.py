# billing/service.py
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Generator, Iterable, Optional, Dict, Any

import stripe
from django.conf import settings
from django.db import transaction

from billing.models import Customer, StripeCustomer

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class StripeConfig:
    api_key: str
    api_version: Optional[str] = None  # e.g. "2024-06-20"


class StripeService:
    """
    Central service for Stripe connections and customer syncing.
    Works with:
      - Customer (canonical person, CI-unique email)
      - StripeCustomer (child rows, one per stripe_customer_id)
    """

    def __init__(self, config: Optional[StripeConfig] = None):
        api_key = (config.api_key if config else None) or getattr(
            settings, "STRIPE_API_KEY", None
        )
        if not api_key:
            raise RuntimeError(
                "Missing STRIPE_API_KEY (settings) or StripeConfig.api_key"
            )
        stripe.api_key = api_key
        if config and config.api_version:
            stripe.api_version = config.api_version

    # ---------- Low-level Stripe fetches ----------
    def get_customer(self, stripe_customer_id: str) -> stripe.Customer:
        return stripe.Customer.retrieve(stripe_customer_id)

    def iter_customers(
        self, limit: int = 100
    ) -> Generator[stripe.Customer, None, None]:
        """
        Generator over all Stripe customers using keyset pagination.
        """
        starting_after = None
        while True:
            page = stripe.Customer.list(
                limit=limit, starting_after=starting_after
            )
            data = page.get("data", [])
            if not data:
                break
            for obj in data:
                yield obj
            if not page.get("has_more"):
                break
            starting_after = data[-1]["id"]

    # ---------- Helpers ----------
    @staticmethod
    def _norm_email(email: Optional[str]) -> str:
        return (email or "").strip()

    @staticmethod
    def _norm_name(name: Optional[str]) -> str:
        return (name or "").strip()

    def _find_or_create_canonical_customer(
        self, email: str, name: str
    ) -> tuple[Customer, bool]:
        """
        Case-insensitive lookup by email. If not found, create.
        NOTE: Can't use get_or_create with __iexact; do a two-step.
        """
        existing = Customer.objects.filter(email__iexact=email).first()
        if existing:
            # Optionally backfill name if we don't have one yet.
            if name and not existing.name:
                existing.name = name
                existing.save(update_fields=["name"])
            return existing, False
        created = Customer.objects.create(email=email, name=name)
        return created, True

    # ---------- Stripe -> DB (single object) ----------
    @transaction.atomic
    def upsert_customer_from_stripe(
        self, s: dict
    ) -> tuple[Customer, Optional[StripeCustomer], bool]:
        """
        Given a Stripe Customer object (dict-like), ensure:
          1) a canonical Customer exists (by email, CI),
          2) a StripeCustomer child row exists for s['id'].
        Returns (customer, stripe_customer_row, created_customer)
        """
        sid = s["id"]
        email = self._norm_email(s.get("email"))
        name = self._norm_name(s.get("name"))

        # If this Stripe ID is already linked, keep local data fresh and exit.
        sc = (
            StripeCustomer.objects.select_related("customer")
            .filter(stripe_customer_id=sid)
            .first()
        )
        if sc:
            cust = sc.customer
            dirty = False
            # If Stripe now has a better name, update our canonical record
            if name and name != cust.name:
                cust.name = name
                dirty = True
            if dirty:
                cust.save(update_fields=["name"])
            return cust, sc, False

        # No existing link: we need a canonical Customer row.
        if email:
            cust, created = self._find_or_create_canonical_customer(
                email=email, name=name
            )
        else:
            # Stripe customer without an email: create a safe placeholder that won't collide.
            placeholder = f"{sid}@placeholder.local"
            cust, created = self._find_or_create_canonical_customer(
                email=placeholder, name=name
            )

        # Create the StripeCustomer child link (one per Stripe ID).
        sc = StripeCustomer.objects.create(
            customer=cust,
            stripe_customer_id=sid,
            email_snapshot=email or "",
        )

        return cust, sc, created

    # ---------- Stripe -> DB (bulk) ----------
    def pull_all_customers(self, dry_run: bool = False) -> dict:
        """
        Pull every Stripe customer into our local DB (upsert).
        """
        created = updated_links = 0
        for s in self.iter_customers():
            if dry_run:
                # Touch fields to validate mapping without DB writes
                _ = s.get("id")
                _ = s.get("email")
                _ = s.get("name")
                continue
            cust, sc, was_created = self.upsert_customer_from_stripe(s)
            if was_created:
                created += 1
            elif sc is not None:
                updated_links += 1
        return {"customers_created": created, "links_created": updated_links}

    # ---------- DB -> Stripe ----------
    def create_or_update_stripe_customer(
        self, customer: Customer
    ) -> stripe.Customer:
        """
        Ensure the local customer has at least one Stripe customer.
        If they already have one (any), update that record's name/email in Stripe.
        If none, create a new Stripe customer and link it (StripeCustomer row).
        """
        # Prefer a real email for Stripe; avoid sending placeholder emails to Stripe if you can.
        email_for_stripe = customer.email
        name_for_stripe = customer.name or None

        linked = customer.stripe_customers.first()

        if linked:
            sc = stripe.Customer.modify(
                linked.stripe_customer_id,
                email=email_for_stripe or None,
                name=name_for_stripe,
                # metadata={"local_customer_id": str(customer.pk)}  # optional
            )
            # Keep email_snapshot fresh (optional)
            if email_for_stripe and linked.email_snapshot != email_for_stripe:
                linked.email_snapshot = email_for_stripe
                linked.save(update_fields=["email_snapshot"])
            return sc

        # Create a new Stripe customer and link it locally
        sc = stripe.Customer.create(
            email=email_for_stripe or None,
            name=name_for_stripe,
            # metadata={"local_customer_id": str(customer.pk)},  # optional
        )
        StripeCustomer.objects.create(
            customer=customer,
            stripe_customer_id=sc["id"],
            email_snapshot=email_for_stripe or "",
        )
        return sc

    def push_all_customers(
        self,
        queryset: Optional[Iterable[Customer]] = None,
        dry_run: bool = False,
    ) -> dict:
        """
        Push local customers to Stripe:
          - If they have a linked StripeCustomer, update it.
          - If they don't, create one and link it.
        """
        qs = (
            queryset
            if queryset is not None
            else Customer.objects.all().iterator()
        )
        created = updated = 0
        for c in qs:
            if dry_run:
                # no-op, but could log or validate fields here
                continue
            pre = bool(c.stripe_customers.exists())
            self.create_or_update_stripe_customer(c)
            if pre:
                updated += 1
            else:
                created += 1
        return {"stripe_created": created, "stripe_updated": updated}

    # ---------- Product/Price mappers ----------
    def _map_stripe_product(self, sp: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "stripe_product_id": sp["id"],
            "name": (sp.get("name") or "").strip()[:255],
            "description": sp.get("description") or "",
            "active": bool(sp.get("active", True)),
            "product_type": (sp.get("type") or "")[:20],  # "good" | "service" | ""
            "shippable": bool(sp.get("shippable") or False),
            "images": sp.get("images") or [],
            "metadata": sp.get("metadata") or {},
        }

    def _map_stripe_price(self, pr: Dict[str, Any]) -> Dict[str, Any]:
        recurring = pr.get("recurring") or {}
        return {
            "stripe_price_id": pr["id"],
            "active": bool(pr.get("active", True)),
            "currency": (pr.get("currency") or "usd")[:10],
            "unit_amount": int(pr.get("unit_amount") or 0),
            "type": (pr.get("type") or "one_time"),
            "recurring_interval": (recurring.get("interval") or ""),
            "recurring_interval_count": recurring.get("interval_count"),
            "trial_period_days": recurring.get("trial_period_days"),
            "tax_behavior": (pr.get("tax_behavior") or ""),
            "livemode": bool(pr.get("livemode") or False),
            "metadata": pr.get("metadata") or {},
        }

    # ---------- Upserts ----------
    @transaction.atomic
    def upsert_product_from_stripe(self, sp: Dict[str, Any]):
        from billing.models import Product  # local import to avoid circulars

        fields = self._map_stripe_product(sp)
        obj, created = Product.objects.select_for_update().get_or_create(
            stripe_product_id=sp["id"], defaults=fields
        )
        if not created:
            dirty = False
            for k, v in fields.items():
                if getattr(obj, k) != v:
                    setattr(obj, k, v)
                    dirty = True
            if dirty:
                obj.save(update_fields=list(fields.keys()))
        return obj, created

    @transaction.atomic
    def upsert_price_from_stripe(self, product_obj, pr: Dict[str, Any]):
        from billing.models import Price  # local import

        fields = self._map_stripe_price(pr)
        obj, created = Price.objects.select_for_update().get_or_create(
            stripe_price_id=pr["id"],
            defaults={**fields, "product": product_obj},
        )
        if not created:
            dirty = False
            # keep the relation correct in case Stripe moved it (rare, but safe)
            if obj.product_id != product_obj.id:
                obj.product = product_obj
                dirty = True
            for k, v in fields.items():
                if getattr(obj, k) != v:
                    setattr(obj, k, v)
                    dirty = True
            if dirty:
                # product may be in update_fields, so include it explicitly
                obj.save(update_fields=["product", *list(fields.keys())])
        return obj, created

    # ---------- Iterators ----------
    def iter_products(self, limit: int = 100, active: bool | None = None):
        """
        Yields Stripe products. If active is not None, filters by active state.
        """
        starting_after = None
        while True:
            params = {"limit": limit}
            if active is not None:
                params["active"] = active
            page = stripe.Product.list(starting_after=starting_after, **params)
            data = page.get("data", [])
            if not data:
                break
            for obj in data:
                yield obj
            if not page.get("has_more"):
                break
            starting_after = data[-1]["id"]

    def iter_prices_for_product(self, stripe_product_id: str, limit: int = 100, active: bool | None = None):
        starting_after = None
        while True:
            params = {"product": stripe_product_id, "limit": limit}
            if active is not None:
                params["active"] = active
            page = stripe.Price.list(starting_after=starting_after, **params)
            data = page.get("data", [])
            if not data:
                break
            for obj in data:
                yield obj
            if not page.get("has_more"):
                break
            starting_after = data[-1]["id"]

    # ---------- Bulk sync ----------
    def pull_catalog(self, active_only: bool = True, sync_prices: bool = True, dry_run: bool = False) -> dict:
        """
        Pull Products (and Prices) from Stripe into the local DB.
        Returns summary stats.
        """
        from billing.models import Product, Price  # local import

        prod_created = prod_updated = 0
        price_created = price_updated = 0

        for sp in self.iter_products(active=(True if active_only else None)):
            if dry_run:
                # Touch key fields to validate mapping
                _ = sp["id"]; _ = sp.get("name"); _ = sp.get("active")
            else:
                prod_obj, was_created = self.upsert_product_from_stripe(sp)
                if was_created:
                    prod_created += 1
                else:
                    prod_updated += 1

                if sync_prices:
                    for pr in self.iter_prices_for_product(sp["id"], active=(True if active_only else None)):
                        pobj, p_created = self.upsert_price_from_stripe(prod_obj, pr)
                        if p_created:
                            price_created += 1
                        else:
                            price_updated += 1

        return {
            "products_created": prod_created,
            "products_updated": prod_updated,
            "prices_created": price_created,
            "prices_updated": price_updated,
            "dry_run": dry_run,
            "active_only": active_only,
        }
