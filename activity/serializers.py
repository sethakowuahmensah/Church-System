# activity/serializers.py
from rest_framework import serializers
from .models import ActivityTracking

class ActivityTrackingSerializer(serializers.ModelSerializer):
    total_attendance = serializers.SerializerMethodField()

    class Meta:
        model = ActivityTracking
        fields = [
            'id', 'activity_date', 'day', 'activity_name', 'speaker',
            'men_attendance', 'women_attendance', 'youth_attendance',
            'children_attendance', 'total_attendance',
            'general_offering', 'special_offering', 'branch_name'
        ]

    def get_total_attendance(self, obj):
        return (
            obj.men_attendance + obj.women_attendance +
            obj.youth_attendance + obj.children_attendance
        )