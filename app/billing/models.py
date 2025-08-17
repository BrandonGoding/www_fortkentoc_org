from django.db import models
from django.db.models.functions import Lower


class Customer(models.Model):
    email = models.EmailField(db_index=True)
    name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("email"), name="uniq_customer_email_ci"
            )
        ]


class StripeCustomer(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="stripe_customers"
    )
    stripe_customer_id = models.CharField(max_length=64, unique=True)
    email_snapshot = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    # Stripe mirrors
    stripe_product_id = models.CharField(max_length=64, unique=True, blank=True, null=True, db_index=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    # “good” or “service” per Stripe (we’ll keep it optional to avoid migration churn)
    product_type = models.CharField(max_length=20, blank=True)  # "good" | "service" | ""
    shippable = models.BooleanField(default=False)
    images = models.JSONField(default=list, blank=True)   # list[str] of URLs from Stripe
    metadata = models.JSONField(default=dict, blank=True) # your own tags/attrs

    # bookkeeping
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["active"]),
            models.Index(fields=["name"]),
        ]

    def __str__(self) -> str:
        return self.name


class Price(models.Model):
    """
    Stripe 'Price' objects; one Product can have many Prices
    (different currencies, recurring intervals, amounts, etc.)
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="prices")

    # Stripe mirrors
    stripe_price_id = models.CharField(max_length=64, unique=True, blank=True, null=True, db_index=True)
    active = models.BooleanField(default=True)
    currency = models.CharField(max_length=10, default="usd")
    unit_amount = models.IntegerField(help_text="Amount in the smallest currency unit (e.g., cents)")
    # one_time vs recurring details (keep recurring fields nullable for one-time)
    type = models.CharField(max_length=20, default="one_time")  # "one_time" | "recurring"
    recurring_interval = models.CharField(max_length=20, blank=True)  # "day" | "week" | "month" | "year"
    recurring_interval_count = models.PositiveIntegerField(null=True, blank=True)
    trial_period_days = models.PositiveIntegerField(null=True, blank=True)

    tax_behavior = models.CharField(max_length=20, blank=True)  # "", "inclusive", "exclusive", "unspecified"
    livemode = models.BooleanField(default=False)
    metadata = models.JSONField(default=dict, blank=True)

    # bookkeeping
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["active"]),
            models.Index(fields=["currency"]),
            models.Index(fields=["type"]),
        ]
        constraints = [
            # Ensure recurring fields are present when type == "recurring"
            models.CheckConstraint(
                name="price_recurring_fields_valid",
                check=(
                    models.Q(type="one_time") |
                    (models.Q(type="recurring") & models.Q(recurring_interval__gt="") & models.Q(recurring_interval_count__isnull=False))
                ),
            ),
        ]

    def __str__(self) -> str:
        label = f"{self.unit_amount} {self.currency}".upper()
        if self.type == "recurring" and self.recurring_interval:
            label += f" / {self.recurring_interval_count or 1} {self.recurring_interval}"
        return f"{self.product.name} – {label}"
