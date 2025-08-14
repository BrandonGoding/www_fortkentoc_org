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
from website.models import Coach, Event, BoardMember, MapCategory, Event, DayPassLink


class HomePageTemplateView(TemplateView):
    template_name = "website/home_page.html"

class ActivitesPageTemplateView(TemplateView):
    template_name = "website/activities_page.html"

class AboutUsTemplateView(TemplateView):
    template_name = "website/about_page.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_members'] = BoardMember.objects.all()
        return context
    
class CoachingProgramsTemplateView(TemplateView):
    template_name = "website/program_page.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context["coaches"] = Coach.objects.all()
        return context

class DayPassesPage(TemplateView):
    template_name = "website/day_pass_page.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context["day_passes"] = DayPassLink.objects.all()
        return context
    
class TrailsTemplateView(TemplateView):
    template_name = "website/trails_page.html"
    
    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["map_types"] = MapCategory.objects.all()
        return context
    
class UpcomingListingPage(TemplateView):
    template_name = "website/event_listing_page.html"
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data( **kwargs)
        # TODO: Only show current events
        context["events"] = Event.objects.all()
        return context

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
