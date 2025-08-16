from __future__ import annotations

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

import time
from datetime import datetime, timedelta, timezone
import stripe

stripe.api_key = settings.STRIPE_API_KEY

# Defaults (override via ?product=...&days=...&max_pages=...)
DEFAULT_PRODUCT_ID = "prod_SjdJEnJcqARz0r"
DEFAULT_DAYS = 90        # only look back this far
DEFAULT_MAX_PAGES = 10    # at 100 sessions/page => max ~500 sessions scanned


def _utc_ts_days_ago(days: int) -> int:
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=max(1, days))
    return int(start.timestamp())


def stripe_buyers(request):
    """
    Render a DataTable of people (name/email) who purchased a specific product
    via Stripe Checkout, within a bounded time window.

    We iterate Checkout Sessions page-by-page (bounded by max_pages) and filter:
      status == complete AND payment_status == paid
    For each matching session, we fetch line items and keep those whose price.product
    equals the requested product_id.
    """
    if not settings.STRIPE_API_KEY:
        return render(
            request,
            "billing/stripe_dashboard.html",
            {"error": "Missing STRIPE_API_KEY in settings/environment."},
            status=500,
        )

    product_id = request.GET.get("product", DEFAULT_PRODUCT_ID)

    days = int(request.GET.get("days", DEFAULT_DAYS))
    max_pages = int(request.GET.get("max_pages", DEFAULT_MAX_PAGES))

    buyers: dict[str, dict] = {}  # key by email when possible; fallback to customer id; else session id

    # Page through Checkout Sessions without unbounded loops
    params = {
        "limit": 100,
        # Narrow by created time to keep this snappy
        "created": {"gte": _utc_ts_days_ago(days)},
        # Expand customer so we avoid extra API calls to fetch names/emails
        "expand": ["data.customer"],
    }

    pages_seen = 0
    last_id = None

    while True:
        if last_id:
            params["starting_after"] = last_id
        sessions = stripe.checkout.Session.list(**params)
   
        pages_seen += 1

        for session in sessions.data:
            # Keep only paid, completed sessions
            if getattr(session, "status", None) != "complete":
                continue
            if getattr(session, "payment_status", None) != "paid":
                continue

            # Pull line items once; find matching product rows
            line_items = stripe.checkout.Session.list_line_items(
                session.id, limit=100, expand=["data.price.product"]
            )

            qty_for_product = 0
            for li in line_items.auto_paging_iter():
                price = getattr(li, "price", None)
                product = getattr(price, "product", None)
                if getattr(product, "id", None) == product_id:
                    qty = getattr(li, "quantity", 0) or 0
                    qty_for_product += int(qty)

            if qty_for_product == 0:
                continue  # This session did not include the target product

            # Identify the person: prefer Checkout's customer_details, else expanded customer
            name = None
            email = None

            # customer_details is captured at Checkout even if no Customer object exists
            cd = getattr(session, "customer_details", None)
            if cd:
                name = getattr(cd, "name", None) or None
                email = getattr(cd, "email", None) or None

            if not email:
                # Fall back to expanded Customer object if present
                cust = getattr(session, "customer", None)
                if cust and isinstance(cust, dict):
                    # When expanded, stripe lib presents as dict-like
                    name = name or cust.get("name") or None
                    email = email or cust.get("email") or None

            # Key: prefer email (best dedupe), else customer id, else session id
            key = email or (getattr(session, "customer", None) or None) or session.id

            # Seen before? Aggregate
            rec = buyers.get(key, {"name": name or "-", "email": email or "-", "quantity": 0, "last": 0})
            rec["name"] = rec["name"] or name or "-"
            rec["email"] = rec["email"] or email or "-"
            rec["quantity"] += qty_for_product
            rec["last"] = max(rec["last"], int(getattr(session, "created", 0) or 0))
            buyers[key] = rec

        if not sessions.has_more:
            break
        last_id = sessions.data[-1].id

        if pages_seen >= max_pages:
            break  # hard stop to avoid long loops

    # Flatten + sort by last purchase desc
    rows = sorted(buyers.values(), key=lambda r: r["last"], reverse=True)

    return render(
        request,
        "billing/stripe_dashboard.html",
        {
            "buyers": rows,
            "product_id": product_id,
            "days": days,
            "max_pages": max_pages,
        },
    )


# Optional stub — safe to keep
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    secret = settings.STRIPE_WEBHOOK_SECRET
    if not secret:
        return HttpResponseBadRequest("Webhook secret not configured")
    try:
        stripe.Webhook.construct_event(payload, sig_header, secret)
    except Exception as exc:
        return HttpResponseBadRequest(str(exc))
    return HttpResponse(status=200)
