# pastor/models.py
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from authentication.models import ChurchUser


class Pastor(models.Model):
    first_name = models.CharField(max_length=100, default="Unknown")
    last_name = models.CharField(max_length=100, default="Pastor")
    email_address = models.EmailField(unique=True, default="", blank=True)
    phone_number = models.CharField(max_length=15, default="", blank=True)
    whatsapp_number = models.CharField(max_length=15, default="", blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')],
        default='male'
    )
    age_group = models.CharField(
        max_length=20,
        choices=[
            ('youth', 'Youth'), ('men', 'Men'), ('women', 'Women'), ('children', 'Children')
        ],
        default='men'
    )
    branch_name = models.CharField(max_length=100, default="Unknown Branch", blank=True)
    resident = models.CharField(max_length=100, default="", blank=True)
    marital_status = models.CharField(
        max_length=20,
        choices=[
            ('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')
        ],
        default='married'
    )
    is_baptized = models.BooleanField(default=True)
    church_user = models.OneToOneField(
        ChurchUser,
        on_delete=models.CASCADE,
        related_name='pastor_profile',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'pastor'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.branch_name})"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


@receiver(post_migrate)
def create_francis_ayeh_pastor(sender, **kwargs):
    if sender.name != 'pastor':
        return

    email = "seth.mensah005@stu.ucc.edu.gh"
    try:
        church_user = ChurchUser.objects.get(email_address=email)
    except ChurchUser.DoesNotExist:
        church_user = ChurchUser.objects.create(
            first_name="Francis",
            last_name="Ayeh",
            email_address=email,
            phone_number="1111111",
            whatsapp_number="11111111",
            gender="male",
            age_group="men",
            branch_name="assakae",
            resident="Fijai",
            marital_status="married",
            is_baptized=True,
            role="pastor",  
            password=make_password("password100")
        )

    try:
        Pastor.objects.get(email_address=email)
    except Pastor.DoesNotExist:
        Pastor.objects.create(
            first_name="Samuel",
            last_name="Nti",
            email_address=email,
            phone_number="1111111",
            whatsapp_number="11111111",
            gender="male",
            age_group="men",
            branch_name="assakae",
            resident="Fijai",
            marital_status="married",
            is_baptized=True,
            church_user=church_user
        )