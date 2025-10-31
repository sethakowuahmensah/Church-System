# authentication/serializers.py
from rest_framework import serializers
from django.db import models
from .models import ChurchUser
from django.utils import timezone
from datetime import timedelta
import random

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)
    branch_name = serializers.ChoiceField(choices=ChurchUser.BRANCH_CHOICES)

    class Meta:
        model = ChurchUser
        fields = [
            'first_name', 'last_name', 'email_address', 'phone_number',
            'whatsapp_number', 'gender', 'age_group', 'branch_name',
            'resident', 'marital_status', 'is_baptized', 'password',
            'confirm_password'
        ]

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')
        user = ChurchUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()  # full_name or email_address
    branch_name = serializers.ChoiceField(choices=ChurchUser.BRANCH_CHOICES)
    password = serializers.CharField(write_only=True)
    method = serializers.ChoiceField(choices=[('email', 'Email'), ('phone', 'Phone')], required=False, default='email')

    def validate(self, data):
        identifier = data['identifier']
        branch_name = data['branch_name']
        password = data['password']
        method = data.get('method', 'email')

        try:
            if '@' in identifier:
                user = ChurchUser.objects.get(email_address=identifier, branch_name=branch_name)
            else:
                # Split name into parts
                name_parts = identifier.strip().split()
                if len(name_parts) < 2:
                    raise serializers.ValidationError("Full name must include first and last name.")
                first_name = name_parts[0]
                last_name = ' '.join(name_parts[1:])
                user = ChurchUser.objects.get(
                    first_name__iexact=first_name,
                    last_name__iexact=last_name,
                    branch_name=branch_name
                )
        except ChurchUser.DoesNotExist:
            raise serializers.ValidationError("User not found with given credentials.")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password.")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        data['user'] = user
        data['method'] = method
        return data


class OTPRequestSerializer(serializers.Serializer):
    identifier = serializers.CharField()  # email or phone
    branch_name = serializers.ChoiceField(choices=ChurchUser.BRANCH_CHOICES)
    method = serializers.ChoiceField(choices=[('email', 'Email'), ('phone', 'Phone')])

    def validate(self, data):
        identifier = data['identifier']
        branch_name = data['branch_name']
        method = data['method']

        try:
            if '@' in identifier:
                user = ChurchUser.objects.get(email_address=identifier, branch_name=branch_name)
            else:
                user = ChurchUser.objects.get(phone_number=identifier, branch_name=branch_name)
        except ChurchUser.DoesNotExist:
            raise serializers.ValidationError("User not found with given credentials.")

        data['user'] = user
        return data


# UPDATED: Allow verification by full name OR email
class OTPVerifySerializer(serializers.Serializer):
    identifier = serializers.CharField()  # full name OR email_address
    branch_name = serializers.ChoiceField(choices=ChurchUser.BRANCH_CHOICES)
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        identifier = data['identifier']
        branch_name = data['branch_name']
        otp = data['otp']

        try:
            if '@' in identifier:
                # Verify by email
                user = ChurchUser.objects.get(email_address=identifier, branch_name=branch_name)
            else:
                # Verify by full name
                name_parts = identifier.strip().split()
                if len(name_parts) < 2:
                    raise serializers.ValidationError("Please provide both first and last name.")
                first_name = name_parts[0]
                last_name = ' '.join(name_parts[1:])
                user = ChurchUser.objects.get(
                    first_name__iexact=first_name,
                    last_name__iexact=last_name,
                    branch_name=branch_name
                )
        except ChurchUser.DoesNotExist:
            raise serializers.ValidationError("Invalid user details.")

        # Check OTP
        if not user.otp or user.otp != otp or user.otp_is_used or user.otp_expires_at < timezone.now():
            raise serializers.ValidationError("Invalid or expired OTP.")

        data['user'] = user
        return data


class PasswordResetRequestSerializer(serializers.Serializer):
    email_address = serializers.EmailField()

    def validate_email_address(self, value):
        if not ChurchUser.objects.filter(email_address=value).exists():
            raise serializers.ValidationError("No user with this email.")
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8)
    confirm_password = serializers.CharField()

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data