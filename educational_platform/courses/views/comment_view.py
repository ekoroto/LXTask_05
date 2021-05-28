from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from courses.models.comment import Comment
from courses.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    permission_classes = (IsAuthenticated, )
