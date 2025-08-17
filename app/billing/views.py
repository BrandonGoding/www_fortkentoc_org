from __future__ import annotations

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from billing.utils import utc_ts_days_ago
from billing.service import StripeService


class StripeBuyerTemplateView(TemplateView):
    template_name = "billing/stripe_dashboard.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["stripe_public_key"] = settings.STRIPE_PUBLIC_KEY
    #     context["default_product_id"] = StripeService.DEFAULT_PRODUCT_ID
    #     context["default_days"] = StripeService.DEFAULT_DAYS
    #     context["default_max_pages"] = StripeService.DEFAULT_MAX_PAGES
    #     context["utc_ts_days_ago"] = utc_ts_days_ago
    #     return context

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
