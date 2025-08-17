from django.db import models
from django.db.models.functions import Lower


# Create your models here.
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
