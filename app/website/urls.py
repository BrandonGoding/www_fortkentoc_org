from django.urls import path
from django.views.generic import TemplateView
from website import views as website_views

app_name = "website"

urlpatterns = [
    path("", website_views.HomePageTemplateView.as_view(), name="home"),
    path(
        "activities/",
        website_views.ActivitesPageTemplateView.as_view(),
        name="activities",
    ),
    path(
        "about-us/",
        website_views.AboutUsTemplateView.as_view(),
        name="about_us",
    ),
    path(
        "coaching-programs/",
        website_views.CoachingProgramsTemplateView.as_view(),
        name="coaching-programs",
    ),
    path(
        "day-passes/", website_views.DayPassesPage.as_view(), name="day-passes"
    ),
    path(
        "event-calendar",
        TemplateView.as_view(template_name="website/event_calendar.html"),
        name="event-calendar",
    ),
    path(
        "facilities/",
        website_views.TemplateView.as_view(
            template_name="website/facility_page.html"
        ),
        name="facilities",
    ),
    path(
        "location/",
        website_views.TemplateView.as_view(
            template_name="website/location_page.html"
        ),
        name="location",
    ),
    path(
        "memberships/",
        TemplateView.as_view(template_name="website/membership_page.html"),
        name="memberships",
    ),
    path(
        "policies-and-safety/",
        website_views.TemplateView.as_view(
            template_name="website/policies_page.html"
        ),
        name="policies-and-safety",
    ),
    path(
        "rentals/",
        TemplateView.as_view(template_name="website/rentals_page.html"),
        name="rentals",
    ),
    path("trails/", website_views.TrailsTemplateView.as_view(), name="trails"),
    path(
        "upcoming-events/",
        website_views.UpcomingListingPage.as_view(),
        name="upcoming-events",
    ),
    path(
        "api/calendar-events/",
        website_views.calendar_events,
        name="calendar-events",
    ),
    path(
        "partials/activity/<slug:slug>/",
        website_views.ActivitiesDetailView.as_view(),
        name="activity_partial",
    ),
    path("partials/empty/", website_views.empty_route, name="empty_route"),
    path(
        "partials/webcam/", website_views.webcam_partial, name="webcam_modal"
    ),
    path(
        "partials/coach/<int:coach_id>/",
        website_views.CoachDetailsView.as_view(),
        name="coach_modal",
    ),
]
