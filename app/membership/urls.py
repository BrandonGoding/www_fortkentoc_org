from django.urls import path
from django.views.generic import TemplateView

from membership import views as membership_views
from django.views.decorators.csrf import csrf_exempt

app_name = "memberships"

urlpatterns = [
    path(
        "onboarding/membership-type/",
        membership_views.membership_form_step_1,
        name="onboarding_membership_type_partial",
    ),
    path(
        "onboarding/member-info/",
        membership_views.membership_form_step_2,
        name="onboarding_member_partial",
    ),
    path(
        "onboarding/activities-enjoyed/",
        membership_views.membership_form_step_3,
        name="onboarding_activities_enjoyed_partial",
    ),
    path(
        "onboarding/confirmation/",
        membership_views.membership_form_step_4,
        name="onboarding_confirmation_partial",
    ),
    path(
        "onboarding/member-info/member-name/",
        membership_views.MembershipFormNameField.as_view(),
        name="name_fields",
    ),
    path(
        "onboarding/complete/",
        TemplateView.as_view(template_name="website/welcome_new_member.html"),
        name="welcome_new_member",
    ),
    path(
        "onboarding/canceled/",
        TemplateView.as_view(template_name="website/membership_canceled.html"),
        name="canceled",
    ),
    path(
        "onboarding/stripe-callback/",
        membership_views.membership_stripe_callback_url,
        name="stripe-callback",
    ),
]
