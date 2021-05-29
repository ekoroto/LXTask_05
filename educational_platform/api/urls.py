from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from courses.views.comment_view import CommentViewSet
from courses.views.course_view import CourseViewSet
from courses.views.homework_view import HomeworkViewSet
from courses.views.lecture_view import LectureViewSet
from courses.views.rating_view import RatingViewSet
from courses.views.task_view import TaskViewSet
from users.views.user_view import UserViewSet


router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'course', CourseViewSet)
router.register(r'homework', HomeworkViewSet)
router.register(r'lecture', LectureViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'task', TaskViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'auth/', include('rest_framework.urls')),
    path(r'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
