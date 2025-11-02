# activity/models.py
from django.db import models

class ActivityTracking(models.Model):
    activity_date = models.DateField()
    day = models.CharField(max_length=10)  # e.g., "Sunday"
    speaker = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=150)
    men_attendance = models.PositiveIntegerField(default=0)
    women_attendance = models.PositiveIntegerField(default=0)
    youth_attendance = models.PositiveIntegerField(default=0)
    children_attendance = models.PositiveIntegerField(default=0)
    general_offering = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    special_offering = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # REQUIRED: Every activity belongs to a branch
    branch_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activity_tracking'
        ordering = ['-activity_date']
        verbose_name = 'Activity Tracking'
        verbose_name_plural = 'Activity Tracking'

    def __str__(self):
        return f"{self.activity_name} - {self.activity_date} ({self.branch_name})"