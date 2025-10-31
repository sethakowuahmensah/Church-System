# expenses/urls.py
from django.urls import path
from .views import ChurchExpensesListCreateView, ChurchExpensesDetailView

urlpatterns = [
    path('expenses/', ChurchExpensesListCreateView.as_view(), name='expenses-list-create'),
    path('expenses/<int:id>/', ChurchExpensesDetailView.as_view(), name='expenses-detail'),
]