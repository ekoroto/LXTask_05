from django.db import models

from .homework import Homework


class Rating(models.Model):
    value = models.PositiveIntegerField()
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Task: ' + str(self.homework.task.name) + ' Student: ' + str(self.homework.student.username)
