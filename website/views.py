from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView

from website.forms import ContactForm
from website.models import Coach, Testimonial, EventPage


def empty_route(request):
    return HttpResponse("")


def webcam_partial(request):
    return render(request, "website/partials/webcam_modal_partial.html")


def contact_thank_you(request):
    return render(request, "website/partials/contact_form_thank_you.html")


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(
                reverse("website:contact_form_thank_you")
            )
    else:
        form = ContactForm()
    return render(
        request, "website/partials/contact_form.html", {"form": form}
    )


class ProgramsPage(TemplateView):
    template_name = "website/programs.html"

    def get_context_data(self, **kwargs):
        context = super(ProgramsPage, self).get_context_data(**kwargs)
        context["coaches"] = Coach.objects.all()
        return context


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


class EventDetailView(DetailView):
    model = EventPage
    template_name = "website/event_page.html"

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        current_event = self.get_object()
        context["upcoming_events"] = EventPage.objects.exclude(
            pk=current_event.pk
        ).order_by("date")
        return context


class MembershipsPage(TemplateView):
    template_name = "website/memberships.html"

    def get_context_data(self, **kwargs):
        context = super(MembershipsPage, self).get_context_data(**kwargs)
        context["testimonials"] = Testimonial.objects.all()
        return context


class DayPassesPage(TemplateView):
    template_name = "website/day_passes.html"
