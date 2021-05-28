from rest_framework import viewsets, permissions

from users.models.user import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('post',)
    queryset = User.objects.all()
    serializer_class = UserSerializer
