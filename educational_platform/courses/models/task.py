from django.db import models

from .lecture import Lecture


class Task(models.Model):
    topic = models.CharField(max_length=200)
    description = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
