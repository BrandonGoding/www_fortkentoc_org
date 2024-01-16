from django.urls import path
from membership import views as membership_views

app_name = "memberships"

urlpatterns = [
    path("onboarding/membership-type/", membership_views.membership_form_step_1, name="onboarding_membership_type_partial"),
    path("onboarding/member-info/", membership_views.membership_form_step_2, name="onboarding_member_partial"),
    path("onboarding/activities-enjoyed/", membership_views.membership_form_step_3, name="onboarding_activities_enjoyed_partial"),
    path("onboarding/confirmation/", membership_views.membership_form_step_4, name="onboarding_confirmation_partial"),
]
