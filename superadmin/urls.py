# superadmin/urls.py
from django.urls import path
from .views import (
    SuperAdminProfileView,
    ChurchUserListCreateView, ChurchUserDetailView,
    ChurchMemberListCreateView, ChurchMemberDetailView,
    BranchSecretaryListCreateView, BranchSecretaryDetailView,
    PastorListCreateView, PastorDetailView,
    ActivityTrackingListCreateView, ActivityTrackingDetailView,
    ExpenseListCreateView, ExpenseDetailView,
    TitheReturnListCreateView, TitheReturnDetailView
)

urlpatterns = [
    path('profile/', SuperAdminProfileView.as_view(), name='superadmin-profile'),

    path('users/', ChurchUserListCreateView.as_view(), name='superadmin-users'),
    path('users/<int:pk>/', ChurchUserDetailView.as_view(), name='superadmin-user-detail'),

    path('members/', ChurchMemberListCreateView.as_view(), name='superadmin-members'),
    path('members/<int:pk>/', ChurchMemberDetailView.as_view(), name='superadmin-member-detail'),

    path('secretaries/', BranchSecretaryListCreateView.as_view(), name='superadmin-secretaries'),
    path('secretaries/<int:pk>/', BranchSecretaryDetailView.as_view(), name='superadmin-secretary-detail'),

    path('pastors/', PastorListCreateView.as_view(), name='superadmin-pastors'),
    path('pastors/<int:pk>/', PastorDetailView.as_view(), name='superadmin-pastor-detail'),

    path('activities/', ActivityTrackingListCreateView.as_view(), name='superadmin-activities'),
    path('activities/<int:pk>/', ActivityTrackingDetailView.as_view(), name='superadmin-activity-detail'),

    path('expenses/', ExpenseListCreateView.as_view(), name='superadmin-expenses'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='superadmin-expense-detail'),

    path('tithes/', TitheReturnListCreateView.as_view(), name='superadmin-tithes'),
    path('tithes/<int:pk>/', TitheReturnDetailView.as_view(), name='superadmin-tithe-detail'),
]