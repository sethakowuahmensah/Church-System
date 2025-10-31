# tithe_returns/models.py
from django.db import models
from authentication.models import ChurchUser  # Adjust if app name differs

class TitheReturn(models.Model):
    tithe_date = models.DateField()
    day = models.CharField(max_length=10)  # e.g., "Sunday"
    member = models.ForeignKey(
        ChurchUser,
        on_delete=models.PROTECT,
        related_name='tithe_returns'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receiver = models.CharField(max_length=100)  # e.g., "Pastor John"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tithe_returns'
        ordering = ['-tithe_date']
        verbose_name = 'Tithe Return'
        verbose_name_plural = 'Tithe Returns'

    def __str__(self):
        return f"{self.member.get_full_name()} - {self.tithe_date} - GHS {self.amount}"

    @property
    def member_name(self):
        return self.member.get_full_name()