from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from website import views as website_views

app_name = "website"

urlpatterns = [
    path(
        "api/calendar-events/",
        website_views.calendar_events,
        name="calendar-events",
    ),
    path(
        "calendar/",
        TemplateView.as_view(template_name="website/event_calendar.html"),
        name="calendar",
    ),
    path(
        "partials/activity/<slug:slug>/",
        website_views.ActivityDetailView.as_view(),
        name="activity_partial",
    ),
    path(
        "paritals/subscribe/",
        website_views.process_subscribe_form,
        name="subscribe",
    ),
    path(
        "partials/subscribe/thank-you/",
        TemplateView.as_view(
            template_name="website/cta/email_list_thank_you.html"
        ),
        name="subscribe_thank_you",
    ),
    path("partials/empty/", website_views.empty_route, name="empty_route"),
    path(
        "partials/webcam/", website_views.webcam_partial, name="webcam_modal"
    ),
    path(
        "partials/coach/<slug:slug>/",
        website_views.CoachDetailView.as_view(),
        name="coach_modal",
    ),
    path(
        "partials/contact-form/",
        website_views.contact_form,
        name="contact_form",
    ),
    path(
        "partials/contact-form/thank-you/",
        website_views.contact_thank_you,
        name="contact_form_thank_you",
    ),
]
