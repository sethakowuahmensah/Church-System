# activity/urls.py
from django.urls import path
from .views import MemberActivityListView

urlpatterns = [
    path('me/activities/', MemberActivityListView.as_view(), name='member-activities'),
]