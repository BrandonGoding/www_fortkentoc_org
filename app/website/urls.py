from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from website import views as website_views

app_name = "website"

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="website/home_page.html"),
        name="home",
    ),
    path(
        "activities/",
        website_views.ActivitiesTemplateView.as_view(),
        name="activities",
    ),
    path(
        "programs/",
        website_views.ProgramsTemplateView.as_view(),
        name="programs",
    ),
    path(
        "api/calendar-events/",
        website_views.calendar_events,
        name="calendar-events",
    ),
    path("about-us/", website_views.AboutUsView.as_view(), name="about_us"),
    path(
        "day-passes/",
        website_views.DayPassesTemplateView.as_view(),
        name="day-passes",
    ),
    path(
        "memberships/",
        website_views.MembershipTemplateView.as_view(),
        name="memberships",
    ),
    path(
        "calendar/",
        TemplateView.as_view(template_name="website/event_calendar.html"),
        name="calendar",
    ),
    path(
        "events/",
        website_views.EventsListView.as_view(),
        name="events",
    ),
    path(
        "events/past/",
        website_views.PastEventsListView.as_view(),
        name="past-events",
    ),
    path(
        "facilities/",
        TemplateView.as_view(template_name="website/facility_page.html"),
        name="facilities",
    ),
    path(
        "location/",
        TemplateView.as_view(template_name="website/location_page.html"),
        name="location",
    ),
    path(
        "rentals/",
        TemplateView.as_view(template_name="website/rentals_page.html"),
        name="rentals",
    ),
    path(
        "trails/",
        TemplateView.as_view(template_name="website/trails_page.html"),
        name="trails",
    ),
    path(
        "partials/activity/<slug:slug>/",
        website_views.ActivitiesDetailView.as_view(),
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
    path(
        "policies/",
        TemplateView.as_view(template_name="website/policies_page.html"),
        name="policies",
    ),
    path(
        "events/usba-nationals/",
        TemplateView.as_view(template_name="website/usba_nationals_2024.html"),
        name="usba_nationals",
    ),
]
