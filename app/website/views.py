from datetime import datetime

from django.core.mail import BadHeaderError, send_mail
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, TemplateView

from website.forms import ContactForm, SimpleSubscribeForm
from website.models import ActivityPage, Coach, EventDatePage, BoardMember


class AboutTemplateView(TemplateView):
    template_name = "website/about_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_members'] = BoardMember.objects.all()
        return context


class PoliciesTemplateView(TemplateView):
    template_name = "website/policies_page.html"


class FacilitiesTemplateView(TemplateView):
    template_name = "website/facility_page.html"


class LocationTemplateView(TemplateView):
    template_name = "website/location_page.html"


class RentalsTemplateView(TemplateView):
    template_name = "website/rentals_page.html"


class TrailsTemplateView(TemplateView):
    template_name = "website/trails_page.html"


def empty_route(request):
    return HttpResponse("")


def webcam_partial(request):
    return render(request, "website/partials/webcam_modal_partial.html")


def calendar_events(request):
    try:
        start_date_str = request.GET.get("start", "")
        end_date_str = request.GET.get("end", "")
        start_date = (
            datetime.fromisoformat(start_date_str) if start_date_str else None
        )
        end_date = (
            datetime.fromisoformat(end_date_str) if end_date_str else None
        )
        events = []
        for event in EventDatePage.objects.filter(
            date__range=[start_date.date(), end_date.date()]
        ):
            print(event)
            events.append(
                {
                    "title": event.get_parent().title,
                    "start": event.date.strftime("%Y-%m-%d"),
                    "color": "rgb(119 29 29)" if event.cancelled else None,
                    "url": event.get_url(),
                }
            )
        return JsonResponse(events, safe=False)
    except ValueError:
        # Handle invalid date format
        return HttpResponseBadRequest("Invalid date format")


def contact_thank_you(request):
    return render(request, "website/partials/contact_form_thank_you.html")


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # The form is valid, so send an email.
            subject = "FKOC Contact Form"
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    "info@fortkentoc.org",
                    ["brandon.h.goding@gmail.com"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponseRedirect(
                reverse("website:contact_form_thank_you")
            )
    else:
        form = ContactForm()
    return render(
        request, "website/partials/contact_form.html", {"form": form}
    )


def process_subscribe_form(request):
    if request.method == "POST":
        form = SimpleSubscribeForm(request.POST)
        if form.is_valid():
            # The form is valid, so send an email.
            subject = "ADD ME TO THE EMAIL LIST"
            body = {
                "email": form.cleaned_data["email"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    "info@fortkentoc.org",
                    ["brandon.h.goding@gmail.com"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponseRedirect(reverse("website:subscribe_thank_you"))
    else:
        form = SimpleSubscribeForm()
    return render(request, "website/cta/email_list.html", {"form": form})


class CoachDetailView(DetailView):
    model = Coach
    template_name = "website/partials/coach_bio.html"

    def get_context_data(self, **kwargs):
        context = super(CoachDetailView, self).get_context_data(**kwargs)
        context["next_coach"] = (
            Coach.objects.filter(pk__gt=self.object.pk).order_by("id").first()
        )
        context["prev_coach"] = (
            Coach.objects.filter(pk__lt=self.object.pk).order_by("-id").first()
        )
        return context


class ActivityDetailView(DetailView):
    model = ActivityPage
    template_name = "website/partials/activity_partial.html"
