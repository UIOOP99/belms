from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import assignment_upload, assignments_homeworklist, assignment_answer_upload,\
    assignment_download, write_message
from django.conf.urls import url


urlpatterns = [
    url(r'^assignment_upload/', assignment_upload.as_view()),
    url(r'^assignment_list/', assignments_homeworklist.as_view()),
    url(r'^assignment_answer_upload/', assignment_answer_upload.as_view()),
    url(r'^assignment_download/', assignment_download.as_view()),
    url(r'^write_message/', write_message.as_view()),

]
