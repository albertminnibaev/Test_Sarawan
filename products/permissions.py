from rest_framework.permissions import BasePermission


# Проверка на то, что пользователь является администратором
class IsAdmin(BasePermission):
    message = 'Вы не являетесь администратром'

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.is_admin
