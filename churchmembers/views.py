# churchmembers/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ChurchMember
from .serializers import MemberProfileSerializer, MemberDashboardSerializer

class MemberProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = MemberProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return ChurchMember.objects.get(user=self.request.user)

    def perform_update(self, serializer):
        member = serializer.save()
        user = member.user
        user.first_name = member.first_name
        user.last_name = member.last_name
        user.phone_number = member.phone_number
        user.whatsapp_number = member.whatsapp_number
        user.gender = member.gender
        user.age_group = member.age_group
        user.resident = member.resident
        user.marital_status = member.marital_status
        user.save(update_fields=[
            'first_name', 'last_name', 'phone_number', 'whatsapp_number',
            'gender', 'age_group', 'resident', 'marital_status'
        ])


class MemberDashboardView(generics.RetrieveAPIView):
    serializer_class = MemberDashboardSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return ChurchMember.objects.get(user=self.request.user)