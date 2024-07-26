from blogs.models import Blog
from django.contrib import admin
from django.core.handlers.wsgi import WSGIHandler
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

admin.site.register(Blog)


def index(request) -> HttpResponse:
    return render(request, "index.html")


urlpatterns = [path("admin/", admin.site.urls), path("", index)]

application = WSGIHandler()
