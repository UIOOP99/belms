from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import assignment_upload
from django.conf.urls import url


urlpatterns = [
    url(r'^assignment_upload/', assignment_upload.as_view()),
]
