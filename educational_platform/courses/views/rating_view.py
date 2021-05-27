from rest_framework import viewsets

from courses.models.rating import Rating
from courses.serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
