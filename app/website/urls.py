from django_distill import distill_path
from django.views.generic import TemplateView

from website import views as website_views
from website.constants import ACTIVITIES, WINTER_SEASON, COACHES


def get_winter_activity_slug():
    for activity in ACTIVITIES:
        if activity.get("season") == WINTER_SEASON:
            yield {"slug": activity.get("slug")}


def get_coach_slug():
    for coach in COACHES:
        yield {"slug": coach.get("slug")}


app_name = "website"

urlpatterns = [
    distill_path(
        "",
        TemplateView.as_view(template_name="website/home_page.html"),
        name="home",
    ),
    distill_path(
        "activities/",
        website_views.ActivitiesTemplateView.as_view(),
        name="activities",
    ),
    distill_path(
        "programs/",
        website_views.ProgramsTemplateView.as_view(),
        name="programs",
    ),
    distill_path(
        "api/calendar-events/",
        website_views.calendar_events,
        name="calendar-events",
    ),
    distill_path(
        "about-us/", website_views.AboutUsView.as_view(), name="about_us"
    ),
    distill_path(
        "day-passes/",
        website_views.DayPassesTemplateView.as_view(),
        name="day-passes",
    ),
    distill_path(
        "memberships/",
        website_views.MembershipTemplateView.as_view(),
        name="memberships",
    ),
    distill_path(
        "calendar/",
        TemplateView.as_view(template_name="website/event_calendar.html"),
        name="calendar",
    ),
    distill_path(
        "events/",
        website_views.EventsListView.as_view(),
        name="events",
    ),
    distill_path(
        "events/past/",
        website_views.PastEventsListView.as_view(),
        name="past-events",
    ),
    distill_path(
        "facilities/",
        TemplateView.as_view(template_name="website/facility_page.html"),
        name="facilities",
    ),
    distill_path(
        "location/",
        TemplateView.as_view(template_name="website/location_page.html"),
        name="location",
    ),
    distill_path(
        "rentals/",
        TemplateView.as_view(template_name="website/rentals_page.html"),
        name="rentals",
    ),
    distill_path(
        "trails/",
        TemplateView.as_view(template_name="website/trails_page.html"),
        name="trails",
    ),
    distill_path(
        "partials/activity/<slug:slug>/",
        website_views.ActivitiesDetailView.as_view(),
        name="activity_partial",
        distill_func=get_winter_activity_slug,
    ),
    distill_path(
        "partials/empty/", website_views.empty_route, name="empty_route"
    ),
    distill_path(
        "partials/webcam/", website_views.webcam_partial, name="webcam_modal"
    ),
    distill_path(
        "partials/coach/<slug:slug>/",
        website_views.CoachDetailView.as_view(),
        name="coach_modal",
        distill_func=get_coach_slug,
    ),
    distill_path(
        "policies/",
        TemplateView.as_view(template_name="website/policies_page.html"),
        name="policies",
    ),
    distill_path(
        "events/usba-nationals/",
        TemplateView.as_view(template_name="website/usba_nationals_2024.html"),
        name="usba_nationals",
    ),
]
