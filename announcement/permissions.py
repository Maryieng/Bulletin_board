from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ проверка прав на авторство """
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsAdmin(BasePermission):
    """ проверка прав на администратора """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
