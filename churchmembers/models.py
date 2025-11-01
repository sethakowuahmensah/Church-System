# churchmembers/models.py
from django.db import models
from authentication.models import ChurchUser

class ChurchMember(models.Model):
    # === OneToOne link to ChurchUser ===
    user = models.OneToOneField(
        ChurchUser,
        on_delete=models.CASCADE,
        related_name='member_profile',
        limit_choices_to={'role': 'member'}
    )

    # === EXACT SAME COLUMNS AS ChurchUser WITH DEFAULTS ===
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email_address = models.EmailField(unique=True, default='')
    phone_number = models.CharField(max_length=15, default='')
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True, default=None)
    gender = models.CharField(max_length=10, default='other')
    age_group = models.CharField(max_length=20, default='unknown')
    branch_name = models.CharField(max_length=100, default='')
    resident = models.CharField(max_length=100, default='')
    marital_status = models.CharField(max_length=20, default='single')
    is_baptized = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'churchmembers'
        verbose_name = 'Church Member'
        verbose_name_plural = 'Church Members'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.branch_name})"