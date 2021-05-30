from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from courses.models.homework import Homework
from courses.permissions.student_permissions import StudentAccessPermission
from courses.serializers import HomeworkSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fileds = ('progress',)
    ordering_filter = ('student', 'created_at')

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (IsAuthenticated, )
        else:
            self.permission_classes = (IsAuthenticated, StudentAccessPermission)

        return super(HomeworkViewSet, self).get_permissions()
