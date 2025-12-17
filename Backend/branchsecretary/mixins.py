# branchsecretary/mixins.py
from django.db.models import Q
from rest_framework import permissions


class BranchFilterMixin:
    """
    Filters queryset to only show data from the secretary's branch.
    """
    def get_queryset(self):
        user = self.request.user
        branch_name = getattr(user, 'branch_name', None)
        if branch_name:
            return self.queryset.filter(branch_name=branch_name)
        return self.queryset.none()