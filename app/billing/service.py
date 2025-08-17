import stripe
from django.conf import settings


# Defaults (override via ?product=...&days=...&max_pages=...)
DEFAULT_PRODUCT_ID = "prod_SjdJEnJcqARz0r"
DEFAULT_DAYS = 90
DEFAULT_MAX_PAGES = 10


class StripeService:
    stripe.api_key = settings.STRIPE_API_KEY