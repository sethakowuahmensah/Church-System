# tithe_returns/serializers.py
from rest_framework import serializers
from .models import TitheReturn


class TitheReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitheReturn
        fields = '__all__'
        read_only_fields = ['recorded_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Auto-set branch_name from secretary's branch
        validated_data['branch_name'] = self.context['request'].user.branch_name
        validated_data['recorded_by'] = self.context['request'].user
        return super().create(validated_data)