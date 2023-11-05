from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from website.models import BoardMember
from website.forms import ContactForm
from django.core.mail import send_mail


def empty_route(request):
    return HttpResponse("")


def webcam_partial(request):
    return render(request, "website/partials/webcam_modal_partial.html")


def coach_partial(request):
    return render(request, "website/partials/coach_bio.html")


def contact_thank_you(request):
    return render(request, "website/partials/contact_form_thank_you.html")


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("website:contact_form_thank_you"))
    else:
        form = ContactForm()
    return render(request, "website/partials/contact_form.html", {"form": form})


class WhoWeArePage(TemplateView):
    template_name = "website/about_us.html"

    def get_context_data(self, **kwargs):
        context = super(WhoWeArePage, self).get_context_data(**kwargs)
        context['board_members'] = BoardMember.objects.all()
        return context

