# billing/management/commands/sync_stripe_customers.py
from __future__ import annotations

import datetime as dt
from typing import Optional

from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import make_aware, get_default_timezone

from billing.models import Customer
from billing.service import StripeService


class Command(BaseCommand):
    help = "Sync customers between Stripe and the local database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--direction",
            choices=["pull", "push", "two-way"],
            default="pull",
            help="pull: Stripe -> DB, push: DB -> Stripe, two-way: pull then push",
        )
        parser.add_argument(
            "--dry-run", action="store_true", help="Do not write changes"
        )
        parser.add_argument(
            "--since",
            type=str,
            default=None,
            help="ISO date (YYYY-MM-DD). Only push local customers updated since this date.",
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=0,
            help="Optional max number of local customers to push",
        )

    def handle(self, *args, **options):
        direction: str = options["direction"]
        dry_run: bool = options["dry_run"]
        since: Optional[str] = options["since"]
        limit: int = options["limit"]

        service = StripeService()

        if direction in ("pull", "two-way"):
            self.stdout.write(self.style.MIGRATE_HEADING("Stripe → DB"))
            summary = service.pull_all_customers(dry_run=dry_run)
            # New keys (with fallback to old)
            created = summary.get(
                "customers_created", summary.get("created", 0)
            )
            links = summary.get("links_created", summary.get("updated", 0))
            self.stdout.write(
                f"Pulled: customers_created {created} links_created {links} dry-run={dry_run}"
            )

        if direction in ("push", "two-way"):
            self.stdout.write(self.style.MIGRATE_HEADING("DB → Stripe"))
            qs = Customer.objects.all().order_by("pk")

            if since:
                try:
                    dt_naive = dt.datetime.fromisoformat(since)
                except ValueError as e:
                    raise CommandError(
                        f"--since must be YYYY-MM-DD; got {since!r}"
                    ) from e
                dt_aware = make_aware(dt_naive, get_default_timezone())
                if hasattr(Customer, "updated_at"):
                    qs = qs.filter(updated_at__gte=dt_aware)
                else:
                    qs = qs.filter(created_at__gte=dt_aware)

            if limit and limit > 0:
                qs = qs[:limit]

            summary = service.push_all_customers(queryset=qs, dry_run=dry_run)
            # New keys (with fallback to old)
            created = summary.get("stripe_created", summary.get("created", 0))
            updated = summary.get("stripe_updated", summary.get("updated", 0))
            self.stdout.write(
                f"Pushed: stripe_created {created} stripe_updated {updated} dry-run={dry_run}"
            )

        self.stdout.write(self.style.SUCCESS("Done"))
