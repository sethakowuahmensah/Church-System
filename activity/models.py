# activity/models.py
from django.db import models
from authentication.models import ChurchUser


class ActivityTracking(models.Model):
    activity_date = models.DateField()
    day = models.CharField(max_length=10)
    activity_name = models.CharField(max_length=200)
    speaker = models.CharField(max_length=100, blank=True)
    men_attendance = models.IntegerField(default=0)
    women_attendance = models.IntegerField(default=0)
    youth_attendance = models.IntegerField(default=0)
    children_attendance = models.IntegerField(default=0)
    general_offering = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    special_offering = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_offering = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    branch_name = models.CharField(max_length=100)
    recorded_by = models.ForeignKey(
        ChurchUser, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='recorded_activities'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activity_tracking'

    def __str__(self):
        return f"{self.activity_date} - {self.activity_name}"

    def save(self, *args, **kwargs):
        self.total_offering = self.general_offering + self.special_offering
        super().save(*args, **kwargs)