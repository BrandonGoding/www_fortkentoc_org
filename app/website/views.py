from datetime import datetime

from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView, DetailView

from website.constants import (
    ACTIVITIES,
)
from website.models import Coach, Event


class ActivitiesDetailView(DetailView):
    template_name = "website/partials/activity_partial.html"

    def get_object(self, queryset=None):
        for activity in ACTIVITIES:
            if activity["slug"] == self.kwargs["slug"]:
                return activity
        return None  # Return None if no coach with the given slug is found


class CoachDetailsView(DetailView):
    template_name = "website/partials/coach_bio.html"
    model = Coach
    context_object_name = "object"

    def get_object(self, queryset=None):
        return get_object_or_404(Coach, id=self.kwargs["coach_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coach = self.get_object()
        context["next_coach"] = coach.get_next()
        context["prev_coach"] = coach.get_prev()
        return context


class ProgramDates:
    pass


def empty_route(request):
    return HttpResponse("")


def webcam_partial(request):
    return render(request, "website/partials/webcam_modal_partial.html")


def calendar_events(request):
    event_list = []
    for event in Event.objects.all():
        event_title = event.name
        for session in event.sessions.all():
            event_list.append({"title": event_title, "start": session.date})
    return JsonResponse(event_list, safe=False)
