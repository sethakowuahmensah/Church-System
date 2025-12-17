# pastor/urls.py
from django.urls import path
from .views import (
    PastorProfileView, PastorTitheListView,
    PastorExpenseListView, PastorMemberListView,
    PastorActivityListView
)

urlpatterns = [
    path('profile/', PastorProfileView.as_view(), name='pastor-profile'),
    path('tithes/', PastorTitheListView.as_view(), name='pastor-tithes'),
    path('expenses/', PastorExpenseListView.as_view(), name='pastor-expenses'),
    path('members/', PastorMemberListView.as_view(), name='pastor-members'),
    path('activities/', PastorActivityListView.as_view(), name='pastor-activities'),
]