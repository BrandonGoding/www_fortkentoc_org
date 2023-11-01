from django.http import HttpResponse
from django.shortcuts import render


def empty_route(request):
    return HttpResponse('')


def webcam_partial(request):
    return render(request, 'website/partials/webcam_modal_partial.html')
