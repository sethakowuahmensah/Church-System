# activity/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ActivityTracking
from .serializers import ActivityTrackingSerializer

class MemberActivityListView(generics.ListAPIView):
    """
    Returns only activities from the logged-in member's branch.
    """
    serializer_class = ActivityTrackingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Filter by user's branch
        return ActivityTracking.objects.filter(
            branch_name=user.branch_name
        ).order_by('-activity_date')