# branchsecretary/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from churchmembers.models import ChurchMember
from churchmembers.serializers import ChurchMemberSerializer
from activity.models import ActivityTracking
from activity.serializers import ActivityTrackingSerializer
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer
from tithe_returns.models import TitheReturn
from tithe_returns.serializers import TitheReturnSerializer
from .permissions import IsBranchSecretary
from .mixins import BranchFilterMixin


# ------------------------------------------------------------------
# 1. SECRETARY PROFILE
# ------------------------------------------------------------------
class SecretaryProfileView(generics.RetrieveAPIView):
    permission_classes = [IsBranchSecretary]

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = {
            "id": user.id,
            "full_name": user.get_full_name(),
            "email_address": user.email_address,
            "branch_name": user.branch_name,
            "phone_number": user.phone_number,
            "role": user.role
        }
        return Response(profile)


# ------------------------------------------------------------------
# 2. MEMBERS
# ------------------------------------------------------------------
class MemberListCreateView(BranchFilterMixin, generics.ListCreateAPIView):
    queryset = ChurchMember.objects.all()
    serializer_class = ChurchMemberSerializer
    permission_classes = [IsBranchSecretary]


class MemberDetailView(BranchFilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = ChurchMember.objects.all()
    serializer_class = ChurchMemberSerializer
    permission_classes = [IsBranchSecretary]


# ------------------------------------------------------------------
# 3. ACTIVITIES
# ------------------------------------------------------------------
class ActivityListCreateView(BranchFilterMixin, generics.ListCreateAPIView):
    queryset = ActivityTracking.objects.all()
    serializer_class = ActivityTrackingSerializer
    permission_classes = [IsBranchSecretary]


class ActivityDetailView(BranchFilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityTracking.objects.all()
    serializer_class = ActivityTrackingSerializer
    permission_classes = [IsBranchSecretary]


# ------------------------------------------------------------------
# 4. EXPENSES
# ------------------------------------------------------------------
class ExpenseListCreateView(BranchFilterMixin, generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsBranchSecretary]


class ExpenseDetailView(BranchFilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsBranchSecretary]


# ------------------------------------------------------------------
# 5. TITHES
# ------------------------------------------------------------------
class TitheListCreateView(BranchFilterMixin, generics.ListCreateAPIView):
    queryset = TitheReturn.objects.all()
    serializer_class = TitheReturnSerializer
    permission_classes = [IsBranchSecretary]


class TitheDetailView(BranchFilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = TitheReturn.objects.all()
    serializer_class = TitheReturnSerializer
    permission_classes = [IsBranchSecretary]