from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.TextField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = None
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.user_id


class Course(models.Model):
    course_id = models.TextField(primary_key=True)
    course_title = models.TextField()


class Message(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, null=True)
    content = models.TextField(default=None, null=True)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, default=timezone.now)

    def __str__(self):
        return self.content


class Homework(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    note = models.TextField(default='')
    file = models.FileField(upload_to=None, max_length=100)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
