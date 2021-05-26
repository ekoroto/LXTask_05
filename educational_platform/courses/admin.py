from django.contrib import admin

from .models.course import Course
from .models.lecture import Lecture
from .models.task import Task
from .models.homework import Homework
from .models.rating import Rating
from .models.comment import Comment

# Register your models here.
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Task)
admin.site.register(Homework)
admin.site.register(Rating)
admin.site.register(Comment)
