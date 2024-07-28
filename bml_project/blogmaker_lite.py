from django.contrib import admin
from django.core.handlers.wsgi import WSGIHandler
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("blogs.urls")),
]
application = WSGIHandler()
