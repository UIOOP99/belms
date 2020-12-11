from django.db import models
from django.utils import timezone
# Create your models here.

class Assignment(models.Model):
    user_id = models.TextField()
    course_id = models.TextField()
    file_id = models.TextField()
    description = models.TextField(default='')
    start_date =models.DateTimeField(auto_now=False, auto_now_add=False)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)


class Assignment_answer(models.Model):
    user_id = models.TextField()
    course_id = models.TextField()
    File_id = models.TextField()
    description = models.TextField(default='')
    date_of_upload = models.DateTimeField(auto_now=False, auto_now_add=False)