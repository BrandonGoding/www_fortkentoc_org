from __future__ import annotations

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView

from billing.utils import utc_ts_days_ago
from billing.service import StripeService
from billing.models import Customer
from django.views.generic import ListView
from django.db.models import Q, Count, Prefetch
from billing.models import Customer, Product, Price

class StripeCustomersListView(ListView):
    model = Customer
    template_name = "billing/stripe_customers.html"
    context_object_name = "customers"
    paginate_by = 25  # tweak as you like
    ordering = "-created_at"

    def get_queryset(self):
        qs = (
            Customer.objects.all()
            .order_by(self.ordering)
            .prefetch_related("stripe_customers")  # for template loop of IDs
            .annotate(stripe_id_count=Count("stripe_customers"))
        )

        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(email__icontains=q) | Q(name__icontains=q))

        has_stripe = self.request.GET.get("has_stripe")
        if has_stripe == "yes":
            qs = qs.filter(stripe_customers__isnull=False).distinct()
        elif has_stripe == "no":
            qs = qs.filter(stripe_customers__isnull=True)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        total = Customer.objects.count()
        with_stripe = (
            Customer.objects.filter(stripe_customers__isnull=False)
            .distinct()
            .count()
        )
        without_stripe = total - with_stripe
        ctx.update(
            {
                "q": self.request.GET.get("q", ""),
                "has_stripe": self.request.GET.get("has_stripe", ""),
                "stats": {
                    "total": total,
                    "with_stripe": with_stripe,
                    "without_stripe": without_stripe,
                },
            }
        )
        return ctx


class StripeCatalogListView(ListView):
    """
    Wagtail-admin list of Products with inline Prices.
    """
    model = Product
    template_name = "billing/stripe_catalog.html"
    context_object_name = "products"
    paginate_by = 25
    ordering = "-updated_at"

    def get_queryset(self):
        qs = (
            Product.objects
            .all()
            .order_by(self.ordering)
            .annotate(price_count=Count("prices"))
            .prefetch_related(
                Prefetch(
                    "prices",
                    queryset=Price.objects.order_by("-active", "currency", "unit_amount", "id"),
                )
            )
        )

        q = (self.request.GET.get("q") or "").strip()
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(stripe_product_id__icontains=q) |
                Q(prices__stripe_price_id__icontains=q)
            ).distinct()

        active = self.request.GET.get("active")
        if active == "yes":
            qs = qs.filter(active=True)
        elif active == "no":
            qs = qs.filter(active=False)

        ptype = (self.request.GET.get("type") or "").strip()
        if ptype:
            qs = qs.filter(product_type__iexact=ptype)

        currency = (self.request.GET.get("currency") or "").strip().lower()
        if currency:
            qs = qs.filter(prices__currency__iexact=currency).distinct()

        has_prices = self.request.GET.get("has_prices")
        if has_prices == "yes":
            qs = qs.filter(price_count__gt=0)
        elif has_prices == "no":
            qs = qs.filter(price_count=0)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "q": self.request.GET.get("q", ""),
            "active": self.request.GET.get("active", ""),
            "ptype": self.request.GET.get("type", ""),
            "currency": self.request.GET.get("currency", ""),
            "has_prices": self.request.GET.get("has_prices", ""),
            "stats": {
                "total": Product.objects.count(),
                "active": Product.objects.filter(active=True).count(),
                "inactive": Product.objects.filter(active=False).count(),
                "with_prices": Product.objects.annotate(pc=Count("prices")).filter(pc__gt=0).count(),
                "without_prices": Product.objects.annotate(pc=Count("prices")).filter(pc=0).count(),
            },
        })
        return ctx