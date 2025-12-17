# tithe_returns/models.py
from django.db import models
from authentication.models import ChurchUser


class TitheReturn(models.Model):
    member = models.ForeignKey(
        ChurchUser,
        on_delete=models.CASCADE,
        related_name='tithes'
    )
    tithe_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receiver = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100, default='')  # ← ADDED: REQUIRED FIELD
    recorded_by = models.ForeignKey(
        ChurchUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='recorded_tithes'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tithe_return'

    def __str__(self):
        return f"{self.member.get_full_name()} - {self.amount}"