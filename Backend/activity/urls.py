# activity/urls.py
from django.urls import path
from .views import (
    ActivityTrackingListCreateView,
    ActivityTrackingDetailView,
    MemberActivityListView
)

urlpatterns = [
    # Admin CRUD
    path('activities/', ActivityTrackingListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', ActivityTrackingDetailView.as_view(), name='activity-detail'),

    # Member View
    path('me/activities/', MemberActivityListView.as_view(), name='member-activities'),
]