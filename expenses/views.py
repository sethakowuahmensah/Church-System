# expenses/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny  # Change to IsAuthenticated later
from .models import ChurchExpenses
from .serializers import ChurchExpensesSerializer

class ChurchExpensesListCreateView(generics.ListCreateAPIView):
    queryset = ChurchExpenses.objects.all()
    serializer_class = ChurchExpensesSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class ChurchExpensesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChurchExpenses.objects.all()
    serializer_class = ChurchExpensesSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'