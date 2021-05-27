from django.conf import settings
from django.db import models

from .task import Task


def get_file_path(instance, file_name):
    return f'uploads/homeworks/{instance.student.username}/{instance.task.topic}/{file_name}'


class Homework(models.Model):
    DONE = 'DONE'
    NOT_DONE = 'NOT_DONE'
    PROGRESS_CHOICES = (
        (DONE, 'Done'),
        (NOT_DONE, 'Not done'),
    )

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    attachment = models.FileField(upload_to=get_file_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    progress = models.CharField(max_length=20, choices=PROGRESS_CHOICES, default=NOT_DONE)

    class Meta:
        unique_together = ('task', 'student')

    def __str__(self):
        return self.task
