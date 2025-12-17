# authentication/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email_address, password=None, **extra_fields):
        if not email_address:
            raise ValueError("The Email Address field must be set")
        email_address = self.normalize_email(email_address)
        user = self.model(email_address=email_address, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_address, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'bishop')

        return self.create_user(email_address, password, **extra_fields)

class ChurchUser(AbstractBaseUser, PermissionsMixin):
    # Roles
    ROLE_CHOICES = [
        ('bishop', 'Super Admin (Bishop)'),
        ('pastor', 'Pastor'),
        ('secretary', 'Branch Secretary'),
        ('member', 'Church Member'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    AGE_GROUP_CHOICES = [
        ('youth', 'Youth'),
        ('children', 'Children'),
        ('men', 'Men'),
        ('women', 'Women'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]

    BRANCH_CHOICES = [
        ('Tanokrom', 'Tanokrom'),
        ('Kwesimintsim', 'Kwesimintsim'),
        ('Shama', 'Shama'),
        ('Assakae', 'Assakae'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES)
    branch_name = models.CharField(max_length=20, choices=BRANCH_CHOICES, default='Tanokrom')
    resident = models.CharField(max_length=200, blank=True)  # Address
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, blank=True)
    is_baptized = models.BooleanField(default=False)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # OTP Fields (previously in OTPRecord)
    otp = models.CharField(max_length=6, validators=[MinLengthValidator(6)], blank=True, null=True)
    otp_method = models.CharField(max_length=10, choices=[('email', 'Email'), ('phone', 'Phone')], blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    otp_expires_at = models.DateTimeField(blank=True, null=True)
    otp_is_used = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'branch_name']

    def __str__(self):
        return f"{self.get_full_name()} ({self.branch_name})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    @property
    def is_bishop(self):
        return self.role == 'bishop'

    @property
    def is_pastor(self):
        return self.role == 'pastor'

    @property
    def is_secretary(self):
        return self.role == 'secretary'

    @property
    def is_member(self):
        return self.role == 'member'