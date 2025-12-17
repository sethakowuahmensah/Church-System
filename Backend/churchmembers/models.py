# churchmembers/models.py
from django.db import models
from authentication.models import ChurchUser


class ChurchMember(models.Model):
    # These fields are now stored directly on ChurchMember
    first_name = models.CharField(
        max_length=100,
        db_column='first_name',
        default=''  # ← Manual default (Option 2)
    )
    last_name = models.CharField(
        max_length=100,
        db_column='last_name',
        default=''  # ← Manual default (Option 2)
    )
    age_group = models.CharField(
        max_length=20,
        choices=[
            ('youth', 'Youth'),
            ('men', 'Men'),
            ('women', 'Women'),
            ('children', 'Children')
        ],
        default='men',  # ← Manual default (Option 2)
        db_column='age_group'
    )
    branch_name = models.CharField(
        max_length=100,
        db_column='branch_name',
        default=''  # ← Manual default (Option 2)
    )

    # Keep the OneToOne link to ChurchUser (for login, etc.)
    user = models.OneToOneField(
        ChurchUser,
        on_delete=models.CASCADE,
        related_name='churchmember',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'church_member'  # Table name stays the same

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.branch_name})"