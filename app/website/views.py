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
from website.models import ColorChoices, Event, ProgramDate


class AboutUsView(TemplateView):
    template_name = "website/about_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["board_members"] = BOARD_MEMBERS
        return context


class ActivitiesTemplateView(TemplateView):
    template_name = "website/activities_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        winter_activities = []
        for activity in ACTIVITIES:
            if activity.get("season") == WINTER_SEASON:
                winter_activities.append(activity)
        context["winter_activities"] = winter_activities
        summer_activities = []
        for activity in ACTIVITIES:
            if activity.get("season") == OFF_SEASON:
                summer_activities.append(activity)
        context["summer_activities"] = summer_activities
        return context


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


class ProgramsTemplateView(TemplateView):
    template_name = "website/program_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coaches"] = COACHES
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


class EventsListView(TemplateView):
    template_name = "website/event_listing_page.html"
    json_file_path = "website/events.json"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_list = ProgramDate.objects.filter(date__gte=timezone.now()).order_by("date")

        event_list = [
            {
                "title": event.event.title,
                "date": event.date,
                "start_time": event.start_time,
                "end_time": event.end_time,
                "cancelled": event.canceled,
                "category": {
                    "category": event.event.category,
                    "category_color": ColorChoices.color_code(event.event.category.color)
                    if event.event.category
                    else None,
                },
                # "tags": event.get("tags"),
                # "banner_image_url": event.get("banner_image_url"),
                # "url": event.get("url"),
            }
            for event in event_list
        ]
        print(event_list)
        context["events"] = event_list



        # # Filter and sort events
        # upcoming_events = [
        #     event
        #     for event in sorted(event_list, key=lambda e: e["date"])
        #     if event["date"] > datetime.now().date()
        # ]


        return context


class MembershipTemplateView(TemplateView):
    template_name = "website/membership_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PastEventsListView(TemplateView):
    template_name = "website/event_listing_page.html"
    json_file_path = "website/events.json"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_list = []
        data = EVENTS
        for event in data:
            event_title = event["title"]
            for event_date in event["program_dates"]:
                program_date = datetime.strptime(
                    event_date["date"], "%Y-%m-%d"
                ).date()
                event_list.append(
                    {
                        "title": event_title,
                        "date": program_date,
                        "cancelled": event_date.get("cancelled", False),
                        "category": {
                            "category": event.get("category"),
                            "category_color": ColorChoices.get_category_color(
                                event["category"]
                            )
                            if event.get("category")
                            else None,
                        },
                        "tags": event.get("tags"),
                        "show_in_past_events": event.get(
                            "show_in_past_events"
                        ),
                        "url": event.get("url"),
                    }
                )
        event_list = sorted(
            event_list,
            key=lambda event_block: event_block["date"],
            reverse=True,
        )
        context["events"] = [
            event_date
            for event_date in event_list
            if event_date["date"] < datetime.now().date()
            and event_date["show_in_past_events"]
        ]
        return context


def empty_route(request):
    return HttpResponse("")


def webcam_partial(request):
    return render(request, "website/partials/webcam_modal_partial.html")


def calendar_events(request):
    event_list = []
    for event in Event.objects.all():
        event_title = event.title
        for date in event.program_dates.all():
            event_list.append({"title": event_title, "start": date.date})
    return JsonResponse(event_list, safe=False)
