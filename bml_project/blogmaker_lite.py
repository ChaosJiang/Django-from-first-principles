from django.core.handlers.wsgi import WSGIHandler
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def index(request) -> HttpResponse:
    return render(request, "index.html")


urlpatterns = [path("", index)]

application = WSGIHandler()
