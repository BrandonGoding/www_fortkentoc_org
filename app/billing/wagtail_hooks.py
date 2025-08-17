from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.contrib.admin.views.decorators import staff_member_required
from . import views


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        path(
            "stripe/customers/",
            views.StripeCustomersListView.as_view(),
            name="stripe_customers",
        ),
    ]


@hooks.register("register_admin_menu_item")
def register_stripe_menu_item():
    return MenuItem(
        "Stripe Customers",
        reverse("stripe_customers"),
        icon_name="user",
        order=10000,
    )
