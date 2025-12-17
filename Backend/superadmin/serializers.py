# superadmin/serializers.py
from rest_framework import serializers
from authentication.models import ChurchUser
from churchmembers.models import ChurchMember
from branchsecretary.models import BranchSecretary
from pastor.models import Pastor
from activity.models import ActivityTracking
from expenses.models import Expense
from tithe_returns.models import TitheReturn
from .models import SuperAdmin


class SuperAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperAdmin
        fields = '__all__'


class ChurchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchUser
        fields = '__all__'


class ChurchMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchMember
        fields = '__all__'


class BranchSecretarySerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchSecretary
        fields = '__all__'


class PastorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastor
        fields = '__all__'


class ActivityTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTracking
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class TitheReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitheReturn
        fields = '__all__'