from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView


from website.forms import ContactForm, SimpleSubscribeForm

from website.models import Coach, ActivityPage


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