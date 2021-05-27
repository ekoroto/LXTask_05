from rest_framework import viewsets

from courses.models.homework import Homework
from courses.serializers import HomeworkSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
