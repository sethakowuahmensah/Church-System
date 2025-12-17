# pastor/serializers.py
from rest_framework import serializers
from tithe_returns.models import TitheReturn
from expenses.models import Expense
from churchmembers.models import ChurchMember
from activity.models import ActivityTracking  # ← FIXED


class PastorTitheSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitheReturn
        fields = ['id', 'member_name', 'amount', 'date', 'branch_name']


class PastorExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'description', 'amount', 'date', 'branch_name']


class PastorMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchMember
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'branch_name']


class PastorActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTracking  # ← FIXED
        fields = [
            'id', 'activity_date', 'day', 'activity_name', 'speaker',
            'men_attendance', 'women_attendance', 'youth_attendance',
            'children_attendance', 'general_offering', 'special_offering',
            'total_offering', 'branch_name'
        ]