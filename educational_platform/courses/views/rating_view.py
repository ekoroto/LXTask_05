from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from courses.models.rating import Rating
from courses.permissions.teacher_permissions import TeacherAccessPermission
from courses.serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (IsAuthenticated, )
        else:
            self.permission_classes = (IsAuthenticated, TeacherAccessPermission)

        return super(RatingViewSet, self).get_permissions()
