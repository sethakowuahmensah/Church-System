# churchmembers/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny  # Change later
from .models import ChurchMember
from .serializers import ChurchMemberSerializer

class ChurchMemberListCreateView(generics.ListCreateAPIView):
    queryset = ChurchMember.objects.all()
    serializer_class = ChurchMemberSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class ChurchMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChurchMember.objects.all()
    serializer_class = ChurchMemberSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'