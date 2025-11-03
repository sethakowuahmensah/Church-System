# activity/serializers.py
from rest_framework import serializers
from .models import ActivityTracking


class ActivityTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTracking
        fields = '__all__'
        read_only_fields = ['total_offering', 'recorded_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['recorded_by'] = self.context['request'].user
        return super().create(validated_data)