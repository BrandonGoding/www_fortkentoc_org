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
    path("about-us/", website_views.AboutUsView.as_view(), name="about_us"),
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
        website_views.usba_redirect,
        name="usba_nationals"
    ),
]
