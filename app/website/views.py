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
from django.views.generic import ListView, TemplateView

from website.forms import ContactForm, SimpleSubscribeForm


class AboutUsView(TemplateView):
    template_name = "website/about_page.html"

    people = [
        {
            "name": 'Laura Audibert',
            "role": 'President',
            "imageUrl":
                'https://cdn.fortkentoc.org/media/public/images/board-members-35_6Vtw0Gw.2e16d0ba.fill-296x369.jpg',
        },
        {
            "name": 'Paul Kile',
            "role": 'Vice President',
        },
        {
            "name": 'Danielle Reardon',
            "role": 'Secretary',
            "imageUrl":
                'https://cdn.fortkentoc.org/media/public/images/board-members-46_gr5wYex.2e16d0ba.fill-296x369.jpg',
        },
        {
            "name": 'Pat Theriault',
            "role": 'Treasurer',
            "imageUrl":
                'https://cdn.fortkentoc.org/media/public/images/board-members-50_gTzSElr.2e16d0ba.fill-296x369.jpg',
        },
        {
            "name": 'Deb Hedeen',
            "imageUrl":
                'https://cdn.fortkentoc.org/media/public/images/board-members-38_jqAvAVt.2e16d0ba.fill-296x369.jpg',
        },
        {
            "name": 'Jim Marquis',
            "imageUrl":
                'https://cdn.fortkentoc.org/media/public/images/board-members-43.2e16d0ba.fill-296x369.jpg',
        },
        {
            "name": 'Ben Paradis',
            "imageUrl":
                'https://cdn.fortkentoc.org/media/public/images/board-members-53.2e16d0ba.fill-296x369.jpg',
        },
        {
            "name": 'Carl Theriault',
            "imageUrl":
                'https://cdn.fortkentoc.org/media/public/images/board-members-47.2e16d0ba.fill-296x369.jpg',
        },
        {
            "name": 'Brandon Goding',
            "imageUrl":
                'https://cdn.fortkentoc.org/media/public/images/board-members-36_yrFRg68.2e16d0ba.fill-296x369.jpg',
        },
        {
            "name": 'Mike Tanguay',
        },
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_members'] = self.people
        return context


class ProgramsTemplateView(TemplateView):
    template_name = "website/program_page.html"

    people = [
        {
            "name": "Carl Theriault",
            "title": "Program Director",
            "imageUrl": "https://cdn.fortkentoc.org/media/public/images/fort-kent-outdoor-center-coach-car.f3b3db8f.fill-144x144.jpg"
        },
        {
            "name": "Charlie Cobb",
            "title": "Venue Manager/Nordic Coach",
            "imageUrl": "https://cdn.fortkentoc.org/media/public/images/Ski_Pic_GGTCdh4.bbeadf32.fill-144x144.jpg"
        },
        {
            "name": "Matt Michaud",
            "title": "Youth and Masters Biathlon Coach",
            "imageUrl": "https://cdn.fortkentoc.org/media/public/images/fort-kent-outdoor-center-coach-mat.2e16d0ba.fill-144x144_TYLjMTW.jpg"
        },
        {
            "name": "Ben Paradis",
            "title": "Youth and Masters Nordic Coach",
            "imageUrl": "https://cdn.fortkentoc.org/media/public/images/fort-kent-outdoor-center-coach-ben.2e16d0ba.fill-144x144_ksIi8Lr.png"
        },
        {
            "name": "Sarah Ashley",
            "title": "Nordic Coach",
            "imageUrl": "https://cdn.fortkentoc.org/media/public/images/fort-kent-outdoor-center-coach-sar.2e16d0ba.fill-144x144_NIljKbb.jpg"
        },
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coaches'] = self.people
        return context


class EventsListView(ListView):
    template_name = "website/event_listing_page.html"

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     # NEED TO INCORPORATE live().child_of(self) TO FILTER OUT PAST EVENTS
    #     context["events"] = EventDatePage.objects.filter(
    #         date__gte=datetime.date.today(), live=True
    #     ).order_by("date")
    #     context["categories"] = EventCategory.objects.all().order_by("name")
    #     context["tags"] = EventTag.objects.all().order_by("name")
    #     return context


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
        # for event in EventDatePage.objects.filter(
        #     date__range=[start_date.date(), end_date.date()]
        # ):
        #     print(event)
        #     events.append(
        #         {
        #             "title": event.get_parent().title,
        #             "start": event.date.strftime("%Y-%m-%d"),
        #             "color": "rgb(119 29 29)" if event.cancelled else None,
        #             "url": event.get_url(),
        #         }
        #     )
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
                    ["info@fortkentoc.org"],
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
                    ["info@fortkentoc.org"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponseRedirect(reverse("website:subscribe_thank_you"))
    else:
        form = SimpleSubscribeForm()
    return render(request, "website/cta/email_list.html", {"form": form})
