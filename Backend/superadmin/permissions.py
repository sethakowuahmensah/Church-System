# superadmin/permissions.py
from rest_framework import permissions


class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == 'bishop' and
            hasattr(request.user, 'superadmin_profile')
        )