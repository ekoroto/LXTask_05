from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from courses.models.task import Task
from courses.permissions.teacher_permissions import TeacherAccessPermission
from courses.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fileds = ('lecture',)
    ordering_filter = ('created_at',)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (IsAuthenticated, )
        else:
            self.permission_classes = (IsAuthenticated, TeacherAccessPermission)

        return super(TaskViewSet, self).get_permissions()
