# churchmembers/urls.py
from django.urls import path
from .views import ChurchMemberListCreateView, ChurchMemberDetailView

urlpatterns = [
    path('members/', ChurchMemberListCreateView.as_view(), name='member-list-create'),
    path('members/<int:id>/', ChurchMemberDetailView.as_view(), name='member-detail'),
]