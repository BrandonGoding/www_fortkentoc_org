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
            staff_member_required(views.StripeCustomersListView.as_view()),
            name="stripe_customers",
        ),
    ]


@hooks.register("register_admin_menu_item")
def register_stripe_menu_item():
    return MenuItem(
        "Customers",
        reverse("stripe_customers"),
        icon_name="user",
        order=201,
    )


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        path(
            "stripe/catalog/",
            staff_member_required(views.StripeCatalogListView.as_view()),
            name="stripe_catalog",
        ),
    ]


@hooks.register("register_admin_menu_item")
def register_stripe_menu_item():
    return MenuItem(
        "Catalog",
        reverse("stripe_catalog"),
        icon_name="user",
        order=199,
    )
