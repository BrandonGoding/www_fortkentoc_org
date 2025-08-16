from django import template
from datetime import datetime, timezone

register = template.Library()

@register.filter
def cents_to_dollars(value):
    """
    Stripe amounts are in the smallest currency unit (e.g., cents).
    Render as dollars with 2 decimals.
    """
    try:
        if value in (None, "", False):
            return "0.00"
        return f"{int(value) / 100:.2f}"
    except Exception:
        # If it's not an int-like value, just return as-is
        return value

@register.filter
def unix_to_datetime(value):
    """
    Convert a Stripe Unix timestamp (seconds) to an aware datetime.
    Lets you then use the {{ ...|date:"Y-m-d H:i" }} filter.
    """
    try:
        return datetime.fromtimestamp(int(value), tz=timezone.utc)
    except Exception:
        return value
