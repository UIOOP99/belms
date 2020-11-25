from django.db import models


class Message(models.Model):
    userID = models.PositiveIntegerField(max_length=15, primary_key=True)
    date_time = models.DateTimeField()
    content = models.TextField()
