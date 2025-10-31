# activity/urls.py
from django.urls import path
from .views import ActivityTrackingListCreateView, ActivityTrackingDetailView

urlpatterns = [
    path('activities/', ActivityTrackingListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:id>/', ActivityTrackingDetailView.as_view(), name='activity-detail'),
]