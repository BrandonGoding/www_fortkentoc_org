from django.http import HttpResponse
from django.shortcuts import render


def empty_route(request):
    return HttpResponse('')
