# churchmembers/views.py
from rest_framework import generics, permissions
from .models import ChurchMember
from .serializers import MemberProfileSerializer, MemberDashboardSerializer


class MemberProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = MemberProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.churchmember


class MemberDashboardView(generics.RetrieveAPIView):
    serializer_class = MemberDashboardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.churchmember