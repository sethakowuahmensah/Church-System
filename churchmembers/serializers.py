# churchmembers/serializers.py
from rest_framework import serializers
from .models import ChurchMember

class ChurchMemberSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = ChurchMember
        fields = [
            'id', 'user',
            'first_name', 'last_name', 'full_name',
            'email_address', 'phone_number', 'whatsapp_number',
            'gender', 'age_group', 'branch_name', 'resident',
            'marital_status', 'is_baptized',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"