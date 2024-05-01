from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Проверяет, является ли пользователь модератором."""

    def has_permission(self, request, view):
        perm = request.user.groups.filter(name="moders").exists()
        return perm


class IsOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь собственником."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False

