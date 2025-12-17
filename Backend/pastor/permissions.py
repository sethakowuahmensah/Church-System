# pastor/permissions.py
from rest_framework import permissions


class IsPastorAndBranchOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role != 'pastor':
            return False
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        user_branch = request.user.branch_name
        obj_branch = getattr(obj, 'branch_name', None)
        if obj_branch is None:
            if hasattr(obj, 'branch'):
                obj_branch = obj.branch.branch_name
            elif hasattr(obj, 'member'):
                obj_branch = obj.member.branch_name
        return obj_branch == user_branch