from django.db import models
from django.utils import timezone


class Assignment(models.Model):
    user_id = models.TextField()
    course_id = models.TextField()
    file_id = models.TextField()
    description = models.TextField(default='')
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    deadline = models.DateField(auto_now=False, auto_now_add=False)

    objects = models.Manager()


class Assignment_answer(models.Model):
    user_id = models.TextField()
    course_id = models.TextField()
    file_id = models.TextField()
    homework_number_id = models.TextField()
    description = models.TextField(default='')
    date_of_upload = models.DateField(auto_now=False, auto_now_add=False)

    objects = models.Manager()


class Message(models.Model):
    user_id = models.TextField()
    course_id = models.TextField()
    msg = models.TextField(default='')
    date_of_send = models.DateField(auto_now=False, auto_now_add=False)

    objects = models.Manager()
