from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from courses.models.homework import Homework
from courses.permissions.student_permissions import StudentAccessPermission
from courses.serializers import HomeworkSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (IsAuthenticated, )
        else:
            self.permission_classes = (IsAuthenticated, StudentAccessPermission)

        return super(HomeworkViewSet, self).get_permissions()
