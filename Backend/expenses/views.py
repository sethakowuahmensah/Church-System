# expenses/views.py
from rest_framework import generics
from .models import Expense
from .serializers import ExpenseSerializer


class ChurchExpensesListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ChurchExpensesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer