# churchmembers/urls.py
from django.urls import path
from .views import MemberProfileView, MemberDashboardView

urlpatterns = [
    path('me/profile/', MemberProfileView.as_view(), name='member-profile'),
    path('me/dashboard/', MemberDashboardView.as_view(), name='member-dashboard'),
]