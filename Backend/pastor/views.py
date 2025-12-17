# pastor/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tithe_returns.models import TitheReturn
from expenses.models import Expense
from churchmembers.models import ChurchMember
from activity.models import ActivityTracking  # ← FIXED: Use real model

from .permissions import IsPastorAndBranchOnly
from .serializers import (
    PastorTitheSerializer, PastorExpenseSerializer,
    PastorMemberSerializer, PastorActivitySerializer
)


class PastorProfileView(APIView):
    permission_classes = [IsAuthenticated, IsPastorAndBranchOnly]
    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "full_name": user.get_full_name(),
            "email": user.email_address,
            "phone": user.phone_number,
            "branch": user.branch_name,
            "role": "pastor"
        })


class PastorTitheListView(APIView):
    permission_classes = [IsAuthenticated, IsPastorAndBranchOnly]
    def get(self, request):
        tithes = TitheReturn.objects.filter(branch_name=request.user.branch_name)
        serializer = PastorTitheSerializer(tithes, many=True)
        return Response(serializer.data)


class PastorExpenseListView(APIView):
    permission_classes = [IsAuthenticated, IsPastorAndBranchOnly]
    def get(self, request):
        expenses = Expense.objects.filter(branch_name=request.user.branch_name)
        serializer = PastorExpenseSerializer(expenses, many=True)
        return Response(serializer.data)


class PastorMemberListView(APIView):
    permission_classes = [IsAuthenticated, IsPastorAndBranchOnly]
    def get(self, request):
        members = ChurchMember.objects.filter(branch_name=request.user.branch_name)
        serializer = PastorMemberSerializer(members, many=True)
        return Response(serializer.data)


class PastorActivityListView(APIView):
    permission_classes = [IsAuthenticated, IsPastorAndBranchOnly]
    def get(self, request):
        activities = ActivityTracking.objects.filter(branch_name=request.user.branch_name)  # ← FIXED
        serializer = PastorActivitySerializer(activities, many=True)
        return Response(serializer.data)