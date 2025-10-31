# expenses/models.py
from django.db import models

class ChurchExpenses(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=10)  # e.g., "Sunday", "Monday"

    salary_wages = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    utilities = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    visitation_allowance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    electricity = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    transportation = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    communication = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    publicity = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    medicals = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    instrument = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    donations = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    maintenance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    other_expenses = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'church_expenses'
        ordering = ['-date']
        verbose_name = 'Church Expense'
        verbose_name_plural = 'Church Expenses'

    def __str__(self):
        return f"Expenses - {self.date} ({self.day})"

    def total_expenses(self):
        fields = [
            self.salary_wages, self.utilities, self.visitation_allowance,
            self.electricity, self.transportation, self.communication,
            self.publicity, self.medicals, self.instrument,
            self.donations, self.maintenance, self.other_expenses
        ]
        return sum(fields)