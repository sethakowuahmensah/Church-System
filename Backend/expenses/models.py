# expenses/models.py
from django.db import models
from authentication.models import ChurchUser


class Expense(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=10)
    salary_wages = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    utilities = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    rent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    maintenance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    evangelism = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    welfare = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    projects = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    others = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    branch_name = models.CharField(max_length=100)
    recorded_by = models.ForeignKey(
        ChurchUser, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='recorded_expenses'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'expense'

    def __str__(self):
        return f"{self.date} - {self.branch_name}"

    def save(self, *args, **kwargs):
        fields = [
            self.salary_wages, self.utilities, self.rent, self.maintenance,
            self.evangelism, self.welfare, self.projects, self.others
        ]
        self.total = sum(f for f in fields if f)
        super().save(*args, **kwargs)