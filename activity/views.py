# activity/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny  # Change to IsAuthenticated later
from .models import ActivityTracking
from .serializers import ActivityTrackingSerializer

class ActivityTrackingListCreateView(generics.ListCreateAPIView):
    queryset = ActivityTracking.objects.all()
    serializer_class = ActivityTrackingSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class ActivityTrackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityTracking.objects.all()
    serializer_class = ActivityTrackingSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'