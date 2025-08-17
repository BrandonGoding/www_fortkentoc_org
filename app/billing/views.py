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
from django.db.models import Q, Count
from billing.models import Customer


# billing/views.py


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
