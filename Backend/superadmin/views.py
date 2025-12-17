# superadmin/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperAdmin
from .serializers import (
    SuperAdminSerializer, ChurchUserSerializer, ChurchMemberSerializer,
    BranchSecretarySerializer, PastorSerializer, ActivityTrackingSerializer,
    ExpenseSerializer, TitheReturnSerializer
)
from authentication.models import ChurchUser
from churchmembers.models import ChurchMember
from branchsecretary.models import BranchSecretary
from pastor.models import Pastor
from activity.models import ActivityTracking
from expenses.models import Expense
from tithe_returns.models import TitheReturn
from .models import SuperAdmin


class SuperAdminProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    serializer_class = SuperAdminSerializer

    def get_object(self):
        return self.request.user.superadmin_profile


# === Church Users ===
class ChurchUserListCreateView(generics.ListCreateAPIView):
    queryset = ChurchUser.objects.all()
    serializer_class = ChurchUserSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


class ChurchUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChurchUser.objects.all()
    serializer_class = ChurchUserSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


# === Church Members ===
class ChurchMemberListCreateView(generics.ListCreateAPIView):
    queryset = ChurchMember.objects.all()
    serializer_class = ChurchMemberSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


class ChurchMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChurchMember.objects.all()
    serializer_class = ChurchMemberSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


# === Branch Secretaries ===
class BranchSecretaryListCreateView(generics.ListCreateAPIView):
    queryset = BranchSecretary.objects.all()
    serializer_class = BranchSecretarySerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


class BranchSecretaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BranchSecretary.objects.all()
    serializer_class = BranchSecretarySerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


# === Pastors ===
class PastorListCreateView(generics.ListCreateAPIView):
    queryset = Pastor.objects.all()
    serializer_class = PastorSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


class PastorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pastor.objects.all()
    serializer_class = PastorSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


# === Activities ===
class ActivityTrackingListCreateView(generics.ListCreateAPIView):
    queryset = ActivityTracking.objects.all()
    serializer_class = ActivityTrackingSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


class ActivityTrackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityTracking.objects.all()
    serializer_class = ActivityTrackingSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


# === Expenses ===
class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


# === Tithe Returns ===
class TitheReturnListCreateView(generics.ListCreateAPIView):
    queryset = TitheReturn.objects.all()
    serializer_class = TitheReturnSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


class TitheReturnDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TitheReturn.objects.all()
    serializer_class = TitheReturnSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]