from rest_framework.permissions import BasePermission

from users.models.user import User


class TeacherAccessPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.TEACHER
