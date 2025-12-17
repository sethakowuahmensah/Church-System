# activity/views.py
from rest_framework import generics
from .models import ActivityTracking
from .serializers import ActivityTrackingSerializer


# --------------------------------------------------------------
# 1. LIST / CREATE ACTIVITIES (already exists in your code)
# --------------------------------------------------------------
class ActivityTrackingListCreateView(generics.ListCreateAPIView):
    queryset = ActivityTracking.objects.all()
    serializer_class = ActivityTrackingSerializer


# --------------------------------------------------------------
# 2. RETRIEVE / UPDATE / DELETE ONE ACTIVITY (already exists)
# --------------------------------------------------------------
class ActivityTrackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityTracking.objects.all()
    serializer_class = ActivityTrackingSerializer


# --------------------------------------------------------------
# 3. NEW: MEMBER ACTIVITY LIST VIEW (required by your import)
# --------------------------------------------------------------
class MemberActivityListView(generics.ListAPIView):
    """
    List all activities for the member's branch.
    Used by member dashboard.
    """
    serializer_class = ActivityTrackingSerializer

    def get_queryset(self):
        user = self.request.user
        branch_name = getattr(user, 'branch_name', None)
        if branch_name:
            return ActivityTracking.objects.filter(branch_name=branch_name).order_by('-activity_date')
        return ActivityTracking.objects.none()