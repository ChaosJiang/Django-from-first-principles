from blogs.models import Blog, BlogPost
from django.contrib import admin
from django.core.handlers.wsgi import WSGIHandler
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

admin.site.register((Blog, BlogPost))


def index(request) -> HttpResponse:
    return render(request, "index.html")


def blogs(request) -> HttpResponse:
    all_blogs = Blog.objects.all()
    context = {"blogs": all_blogs}
    return render(request, "blogs.html", context)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", blogs, name="blogs"),
    path("", index, name="index"),
]

application = WSGIHandler()
