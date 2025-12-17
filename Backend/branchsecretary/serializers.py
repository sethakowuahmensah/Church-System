# branchsecretary/serializers.py
from rest_framework import serializers
from .models import BranchSecretary
from churchmembers.models import ChurchMember
from activity.models import ActivityTracking
from expenses.models import ChurchExpenses
from tithe_returns.models import TitheReturn

class BranchSecretarySerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    church_user_id = serializers.IntegerField(source='church_user.id', read_only=True)

    class Meta:
        model = BranchSecretary
        fields = [
            'id', 'church_user_id', 'full_name', 'email_address',
            'phone_number', 'whatsapp_number', 'gender', 'age_group',
            'branch_name', 'resident', 'marital_status', 'is_baptized',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_full_name(self, obj):
        return obj.get_full_name()

class ChurchMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchMember
        fields = '__all__'

class ActivityTrackingSerializer(serializers.ModelSerializer):
    total_attendance = serializers.SerializerMethodField()

    class Meta:
        model = ActivityTracking
        fields = '__all__'

    def get_total_attendance(self, obj):
        return obj.men_attendance + obj.women_attendance + obj.youth_attendance + obj.children_attendance

class ChurchExpensesSerializer(serializers.ModelSerializer):
    total_expenses = serializers.ReadOnlyField(source='total_expenses')

    class Meta:
        model = ChurchExpenses
        fields = '__all__'

class TitheReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitheReturn
        fields = '__all__'