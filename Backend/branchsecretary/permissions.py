# branchsecretary/permissions.py
from rest_framework import permissions


class IsBranchSecretary(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'role') and
            request.user.role == 'secretary'
        )