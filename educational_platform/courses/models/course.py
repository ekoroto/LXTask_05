from django.db import models

from .lecture import Lecture
from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=200)
    teachers = models.ManyToManyField(User,
                                      blank=True,
                                      related_name='course_teachers',
                                      limit_choices_to={'role': User.TEACHER})
    students = models.ManyToManyField(User,
                                      blank=True,
                                      related_name='course_students',
                                      limit_choices_to={'role': User.STUDENT})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lectures = models.ManyToManyField(Lecture, blank=True)

    def __str__(self):
        return self.name
