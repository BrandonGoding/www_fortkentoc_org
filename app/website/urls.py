from django.urls import path
from django.views.generic import TemplateView
from website import views as website_views

app_name = "website"

urlpatterns = [
    path(
        "about-us/",
        website_views.AboutUsTemplateView.as_view(),
        name="about_us"
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
