from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    message = "You must be Admin for this validation"

    def has_object_permission(self, request, view, obj):
        return (request.user.is_superuser)