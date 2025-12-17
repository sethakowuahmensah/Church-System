# branchsecretary/urls.py
from django.urls import path
from .views import (
    SecretaryProfileView,
    MemberListCreateView, MemberDetailView,
    ActivityListCreateView, ActivityDetailView,
    ExpenseListCreateView, ExpenseDetailView,
    TitheListCreateView, TitheDetailView
)

urlpatterns = [
    # Profile
    path('profile/', SecretaryProfileView.as_view(), name='secretary-profile'),

    # Members
    path('members/', MemberListCreateView.as_view(), name='secretary-members'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='secretary-member-detail'),

    # Activities
    path('activities/', ActivityListCreateView.as_view(), name='secretary-activities'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='secretary-activity-detail'),

    # Expenses
    path('expenses/', ExpenseListCreateView.as_view(), name='secretary-expenses'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='secretary-expense-detail'),

    # Tithes
    path('tithes/', TitheListCreateView.as_view(), name='secretary-tithes'),
    path('tithes/<int:pk>/', TitheDetailView.as_view(), name='secretary-tithe-detail'),
]