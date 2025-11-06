# Church_system/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('api/auth/', include('authentication.urls')),

    # OTHER APPS (you already have these)
    path('api/activities/', include('activity.urls')),
    path('api/expenses/', include('expenses.urls')),
    path('api/tithe-returns/', include('tithe_returns.urls')),
    path('api/me/', include('churchmembers.urls')),

    # TOKEN
    path('api/token/', include('rest_framework.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/secretary/', include('branchsecretary.urls')),
    path('api/pastor/', include('pastor.urls')),
    path('api/superadmin/', include('superadmin.urls')),
]