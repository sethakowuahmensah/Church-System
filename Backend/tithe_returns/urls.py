# tithe_returns/urls.py
from django.urls import path
from .views import TitheReturnListCreateView, TitheReturnDetailView

urlpatterns = [
    path('tithe-returns/', TitheReturnListCreateView.as_view(), name='tithe-return-list-create'),
    path('tithe-returns/<int:id>/', TitheReturnDetailView.as_view(), name='tithe-return-detail'),
]