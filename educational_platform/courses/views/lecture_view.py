from rest_framework import viewsets

from courses.models.lecture import Lecture
from courses.serializers import LectureSerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
