# churchmembers/serializers.py
from rest_framework import serializers
from .models import ChurchMember
from authentication.models import ChurchUser
from activity.models import ActivityTracking
from activity.serializers import ActivityTrackingSerializer
from tithe_returns.models import TitheReturn


# 1. MEMBER PROFILE
class MemberProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchMember
        fields = [
            'first_name', 'last_name', 'email_address',
            'phone_number', 'whatsapp_number', 'gender',
            'age_group', 'resident', 'marital_status'
        ]
        read_only_fields = ['email_address']


# 2. TITHE HISTORY
class TitheReturnSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitheReturn
        fields = ['tithe_date', 'amount', 'receiver']


# 3. DASHBOARD
class MemberDashboardSerializer(serializers.ModelSerializer):
    tithe_history = serializers.SerializerMethodField()
    branch_activities = serializers.SerializerMethodField()

    class Meta:
        model = ChurchMember
        fields = ['first_name', 'last_name', 'branch_name', 'tithe_history', 'branch_activities']

    def get_tithe_history(self, obj):
        tithes = TitheReturn.objects.filter(member=obj.user).order_by('-tithe_date')[:10]
        return TitheReturnSimpleSerializer(tithes, many=True).data

    def get_branch_activities(self, obj):
        activities = ActivityTracking.objects.filter(branch_name=obj.branch_name).order_by('-activity_date')[:10]
        return ActivityTrackingSerializer(activities, many=True).data


# 4. CHURCH MEMBER (SECRETARY CRUD) — AUTO-CREATE USER
class ChurchMemberSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    email_address = serializers.EmailField(write_only=True, required=True)
    phone_number = serializers.CharField(write_only=True, required=False, allow_blank=True)
    gender = serializers.CharField(write_only=True, required=False)
    age_group = serializers.CharField(write_only=True, required=False)
    marital_status = serializers.CharField(write_only=True, required=False)
    is_baptized = serializers.BooleanField(write_only=True, default=False)
    role = serializers.CharField(write_only=True, default="member")
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = ChurchMember
        fields = [
            'id', 'user', 'branch_name',
            'first_name', 'last_name', 'email_address',
            'phone_number', 'gender', 'age_group',
            'marital_status', 'is_baptized', 'role', 'password'
        ]
        read_only_fields = ['user']

    def create(self, validated_data):
        user_data = {
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'email_address': validated_data.pop('email_address'),
            'phone_number': validated_data.pop('phone_number', ''),
            'gender': validated_data.pop('gender', ''),
            'age_group': validated_data.pop('age_group', ''),
            'branch_name': validated_data.get('branch_name'),
            'marital_status': validated_data.pop('marital_status', ''),
            'is_baptized': validated_data.pop('is_baptized', False),
            'role': validated_data.pop('role', 'member'),
        }
        password = validated_data.pop('password')
        user = ChurchUser.objects.create(**user_data)
        user.set_password(password)
        user.save()
        member = ChurchMember.objects.create(user=user, **validated_data)
        return member