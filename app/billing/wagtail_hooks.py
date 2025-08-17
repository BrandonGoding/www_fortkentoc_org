from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.contrib.admin.views.decorators import staff_member_required
from . import views

@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        path("stripe/buyers/", staff_member_required(views.StripeBuyerTemplateView.as_view()), name="stripe_buyers"),
    ]

@hooks.register("register_admin_menu_item")
def register_stripe_menu_item():
    return MenuItem(
        "BBQ Attendees",
        reverse("stripe_buyers"),
        icon_name="user",
        order=10000,
    )
