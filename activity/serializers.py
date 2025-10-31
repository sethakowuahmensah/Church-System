# activity/serializers.py
from rest_framework import serializers
from .models import ActivityTracking

class ActivityTrackingSerializer(serializers.ModelSerializer):
    total_attendance = serializers.SerializerMethodField()
    total_offering = serializers.SerializerMethodField()

    class Meta:
        model = ActivityTracking
        fields = [
            'id', 'activity_date', 'day', 'speaker', 'activity_name',
            'men_attendance', 'women_attendance', 'youth_attendance', 'children_attendance',
            'general_offering', 'special_offering',
            'total_attendance', 'total_offering',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'total_attendance', 'total_offering']

    def get_total_attendance(self, obj):
        return (
            obj.men_attendance +
            obj.women_attendance +
            obj.youth_attendance +
            obj.children_attendance
        )

    def get_total_offering(self, obj):
        return obj.general_offering + obj.special_offering