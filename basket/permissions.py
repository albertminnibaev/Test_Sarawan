from rest_framework.permissions import BasePermission


# проверка на то, что пользователь является владельцем корзины
class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем корзины, у вас нет права доступа,"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
