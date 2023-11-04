from django.urls import path
from django.views.generic import TemplateView
import website.views as website_views

app_name = "website"

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="website/home_page.html"),
        name="home_page",
    ),
    path("about-us", TemplateView.as_view(template_name="website/about_us.html"), name="about_us"),
    path("facilities", TemplateView.as_view(template_name="website/facilities.html"), name="facilities"),
    path("policies", TemplateView.as_view(template_name="website/policies.html"), name="policies"),
    path("partials/empty", website_views.empty_route, name="empty_route"),
    path("partials/webcam", website_views.webcam_partial, name="webcam_modal"),
    path("partials/contact-form", website_views.contact_form, name="contact_form"),
    path("partials/contact-form/thank-you", website_views.contact_thank_you, name="contact_form_thank_you"),
]
