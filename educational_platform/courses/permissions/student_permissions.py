from rest_framework.permissions import BasePermission

from users.models.user import User


class StudentAccessPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.STUDENT
