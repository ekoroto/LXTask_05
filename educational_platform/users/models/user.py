from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    TEACHER = 'teacher'
    STUDENT = 'student'
    ROLES_CHOICES = (
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLES_CHOICES,
        default=TEACHER
    )
