from django.urls import path
from django.views.generic import TemplateView

from membership import views as membership_views

app_name = "memberships"

urlpatterns = [
    path(
        "onboarding/membership-type/",
        membership_views.MembershipFormStep1View.as_view(),
        name="onboarding_membership_type_partial",
    ),
    path(
        "onboarding/member-info/",
        membership_views.MembershipFormStep2View.as_view(),
        name="onboarding_member_partial",
    ),
    path(
        "onboarding/activities-enjoyed/",
        membership_views.MembershipFormStep3View.as_view(),
        name="onboarding_activities_enjoyed_partial",
    ),
    path(
        "onboarding/confirmation/",
        membership_views.MembershipFormStep4View.as_view(),
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
        membership_views.MembershipStripeCallbackView.as_view(),
        name="stripe-callback",
    ),
]
