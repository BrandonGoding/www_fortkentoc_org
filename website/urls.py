from django.urls import path
from django.views.generic import TemplateView


import website.views as website_views

app_name = "website"

urlpatterns = [
    # path(
    #     "",
    #     website_views.HomePage.as_view(),
    #     name="home_page",
    # ),
#    path("about-us/", website_views.WhoWeArePage.as_view(), name="about_us"),
#    path("day-passes/", website_views.DayPassesPage.as_view(), name="day_passes"),
#    path("events/<slug:slug>/", website_views.EventDetailView.as_view(), name="event_detail"),
#    path("facilities/", TemplateView.as_view(template_name="website/facility_page.html"), name="facilities"),
#    path("location/", TemplateView.as_view(template_name="website/location_page.html"), name="location"),
#    path("memberships/", website_views.MembershipsPage.as_view(), name="memberships"),
#    path("policies/", TemplateView.as_view(template_name="website/policies_page.html"), name="policies"),
    path("partials/empty/", website_views.empty_route, name="empty_route"),
    path("partials/webcam/", website_views.webcam_partial, name="webcam_modal"),
    path("partials/coach/<slug:slug>/", website_views.CoachDetailView.as_view(), name="coach_modal"),
    path("partials/contact-form/", website_views.contact_form, name="contact_form"),
    path("partials/contact-form/thank-you/", website_views.contact_thank_you, name="contact_form_thank_you"),
#    path("programs/", website_views.ProgramsPage.as_view(), name="programs"),
#    path("rentals/", TemplateView.as_view(template_name="website/rentals_page.html"), name="rentals"),
]
