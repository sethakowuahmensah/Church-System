# churchmembers/serializers.py
from rest_framework import serializers
from .models import ChurchMember
from tithe_returns.models import TitheReturn
from activity.models import ActivityTracking
from activity.serializers import ActivityTrackingSerializer

# ----------------------------------------------------------------------
# 1. PROFILE SERIALIZER (Read & Update)
# ----------------------------------------------------------------------
class MemberProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchMember
        fields = [
            'first_name', 'last_name', 'email_address',
            'phone_number', 'whatsapp_number', 'gender',
            'age_group', 'resident', 'marital_status'
        ]
        read_only_fields = ['email_address']  # Email can't be changed


# ----------------------------------------------------------------------
# 2. TITHE HISTORY
# ----------------------------------------------------------------------
class TitheReturnSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitheReturn
        fields = ['tithe_date', 'amount', 'receiver']


# ----------------------------------------------------------------------
# 3. DASHBOARD SERIALIZER (Tithe + Activities)
# ----------------------------------------------------------------------
class MemberDashboardSerializer(serializers.ModelSerializer):
    tithe_history = serializers.SerializerMethodField()
    branch_activities = serializers.SerializerMethodField()

    class Meta:
        model = ChurchMember
        fields = [
            'first_name', 'last_name', 'branch_name',
            'tithe_history', 'branch_activities'
        ]

    def get_tithe_history(self, obj):
        tithes = TitheReturn.objects.filter(member=obj.user).order_by('-tithe_date')
        return TitheReturnSimpleSerializer(tithes, many=True).data

    def get_branch_activities(self, obj):
        activities = ActivityTracking.objects.filter(
            branch_name=obj.branch_name
        ).order_by('-activity_date')[:10]
        return ActivityTrackingSerializer(activities, many=True).data