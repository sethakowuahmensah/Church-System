# expenses/serializers.py
from rest_framework import serializers
from .models import ChurchExpenses

class ChurchExpensesSerializer(serializers.ModelSerializer):
    total_expenses = serializers.SerializerMethodField()

    class Meta:
        model = ChurchExpenses
        fields = [
            'id', 'date', 'day',
            'salary_wages', 'utilities', 'visitation_allowance',
            'electricity', 'transportation', 'communication',
            'publicity', 'medicals', 'instrument',
            'donations', 'maintenance', 'other_expenses',
            'total_expenses',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'total_expenses', 'created_at', 'updated_at']

    def get_total_expenses(self, obj):
        return obj.total_expenses()