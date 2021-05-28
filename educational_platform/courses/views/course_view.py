from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from courses.models.course import Course
from courses.permissions.teacher_permissions import TeacherAccessPermission
from courses.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (IsAuthenticated, )
        else:
            self.permission_classes = (IsAuthenticated, TeacherAccessPermission)

        return super(CourseViewSet, self).get_permissions()
