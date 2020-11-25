from django.db import models

class Message(models.Model):
    userID = models.PositiveIntegerField(primary_key=True)
    content = models.TextField(default='')
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False , null = True)
