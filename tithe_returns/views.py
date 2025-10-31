# tithe_returns/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny  # Change to IsAuthenticated later
from .models import TitheReturn
from .serializers import TitheReturnSerializer

class TitheReturnListCreateView(generics.ListCreateAPIView):
    queryset = TitheReturn.objects.select_related('member').all()
    serializer_class = TitheReturnSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class TitheReturnDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TitheReturn.objects.select_related('member').all()
    serializer_class = TitheReturnSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'