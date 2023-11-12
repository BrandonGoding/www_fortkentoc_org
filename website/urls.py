from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

import website.views as website_views

app_name = "website"

urlpatterns = [
    path(
        "day-passes", website_views.DayPassesPage.as_view(), name="day_passes"
    ),
    path(
        "location",
        TemplateView.as_view(template_name="website/location.html"),
        name="location",
    ),
    path(
        "memberships",
        website_views.MembershipsPage.as_view(),
        name="memberships",
    ),
    path("partials/empty", website_views.empty_route, name="empty_route"),
    path("partials/webcam", website_views.webcam_partial, name="webcam_modal"),
    path(
        "partials/contact-form",
        website_views.contact_form,
        name="contact_form",
    ),
    path(
        "partials/contact-form/thank-you",
        website_views.contact_thank_you,
        name="contact_form_thank_you",
    ),
    path("programs", website_views.ProgramsPage.as_view(), name="programs"),
    path(
        "rentals",
        TemplateView.as_view(template_name="website/rentals.html"),
        name="rentals",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
