# tithe_returns/serializers.py
from rest_framework import serializers
from .models import TitheReturn
from authentication.models import ChurchUser

class ChurchUserSimpleSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = ChurchUser
        fields = ['id', 'first_name', 'last_name', 'full_name', 'email_address']

class TitheReturnSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member.get_full_name', read_only=True)
    member = ChurchUserSimpleSerializer(read_only=True)
    member_id = serializers.PrimaryKeyRelatedField(
        queryset=ChurchUser.objects.all(),
        source='member',
        write_only=True
    )

    class Meta:
        model = TitheReturn
        fields = [
            'id', 'tithe_date', 'day',
            'member', 'member_id', 'member_name',
            'amount', 'receiver',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'member_name', 'created_at', 'updated_at']

    def validate(self, data):
        # Optional: Ensure amount > 0
        if data['amount'] <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return data