from datetime import datetime

from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, DetailView

from website.constants import (
    COACHES,
    BOARD_MEMBERS,
    ACTIVITIES,
    WINTER_SEASON,
    OFF_SEASON,
)


class ActivitiesDetailView(DetailView):
    template_name = "website/partials/activity_partial.html"

    def get_object(self, queryset=None):
        for activity in ACTIVITIES:
            if activity["slug"] == self.kwargs["slug"]:
                return activity
        return None  # Return None if no coach with the given slug is found


class DayPassesTemplateView(TemplateView):
    template_name = "website/day_pass_page.html"

    square_links = [
        {
            "url": "https://buy.stripe.com/dR69Ep4mM0VW5Co4gh",
            "image": "/static/media/public/original_images/DALLE_2023-12-10_12.25.00_-_An_adult_cross_country_skier_gliding_through_a.png",
            "name": "Adult Ski Pass",
            "price": 18,
        },
        {
            "url": "https://buy.stripe.com/28o5o9cTicEE2qc4gi",
            "image": "/static/media/public/original_images/DALLE_2023-12-10_12.34.29_-_A_youth_cross_country_skier_gliding_through_a_.png",
            "name": "Junior Ski Pass",
            "price": 12,
        },
        {
            "url": "https://buy.stripe.com/7sI9EpcTieMMc0MfZ1",
            "image": "/static/media/public/original_images/DALLE_2023-12-10_12.37.47_-_An_adult_snowshoer_trekking_through_a_winter_l.png",
            "name": "Adult Snowshoe Pass",
            "price": 10,
        },
        {
            "url": "https://buy.stripe.com/6oE3g11aA6gg3ug3cg",
            "image": "/static/media/public/original_images/DALLE_2023-12-10_12.39.40_-_A_youth_snowshoer_trekking_through_a_winter_la.png",
            "name": "Junior Snowshoe Pass",
            "price": 5,
        },
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["square_links"] = self.square_links
        return context



class CoachDetailView(DetailView):
    template_name = "website/partials/coach_bio.html"

    def get_object(self, queryset=None):
        for coach in COACHES:
            if coach["slug"] == self.kwargs["slug"]:
                return coach
        return None  # Return None if no coach with the given slug is found


class ProgramDates:
    pass


def empty_route(request):
    return HttpResponse("")


def webcam_partial(request):
    return render(request, "website/partials/webcam_modal_partial.html")


# def calendar_events(request):
#     event_list = []
#     for event in EventPage.objects.all():
#         event_title = event.title
#         for date in event.program_dates.all():
#             event_list.append({"title": event_title, "start": date.date})
#     return JsonResponse(event_list, safe=False)
