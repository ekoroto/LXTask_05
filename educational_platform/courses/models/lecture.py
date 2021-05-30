from django.db import models

from users.models import User


def get_file_path(instance, file_name):
    return f'uploads/lectures/{instance.topic}/{instance.author.first_name} {instance.author.last_name}/ \
        {file_name}'


class Lecture(models.Model):
    topic = models.CharField(max_length=200)
    attachments = models.FileField(upload_to=get_file_path, blank=True, null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               limit_choices_to={'role': User.TEACHER})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic
