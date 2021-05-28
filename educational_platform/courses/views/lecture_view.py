from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from courses.models.lecture import Lecture
from courses.permissions.teacher_permissions import TeacherAccessPermission
from courses.serializers import LectureSerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (IsAuthenticated, )
        else:
            self.permission_classes = (IsAuthenticated, TeacherAccessPermission)

        return super(LectureViewSet, self).get_permissions()
