from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_admin:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user == obj.author:
            return True