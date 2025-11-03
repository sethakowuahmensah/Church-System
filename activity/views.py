# activity/views.py
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import ActivityTracking
from .serializers import ActivityTrackingSerializer

# ------------------------------------------------------------------
# ADMIN: CRUD for ActivityTracking
# ------------------------------------------------------------------
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'super_admin']

class ActivityTrackingListCreateView(generics.ListCreateAPIView):
    queryset = ActivityTracking.objects.all().order_by('-activity_date')
    serializer_class = ActivityTrackingSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ActivityTrackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityTracking.objects.all()
    serializer_class = ActivityTrackingSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# ------------------------------------------------------------------
# MEMBER: View Only Own Branch
# ------------------------------------------------------------------
class MemberActivityListView(generics.ListAPIView):
    serializer_class = ActivityTrackingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ActivityTracking.objects.filter(
            branch_name=user.branch_name
        ).order_by('-activity_date')