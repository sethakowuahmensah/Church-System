# authentication/serializers.py
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import ChurchUser
from django.db.models import Q
import re
from django.utils import timezone


# ----------------------------------------------------------------------
# 1. SIGNUP SERIALIZER
# ----------------------------------------------------------------------
class UserSignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = ChurchUser
        fields = [
            'first_name', 'last_name', 'email_address', 'phone_number',
            'whatsapp_number', 'gender', 'age_group', 'branch_name',
            'resident', 'marital_status', 'is_baptized', 'password',
            'confirm_password', 'role'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        if len(data['password']) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = ChurchUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


# ----------------------------------------------------------------------
# 2. LOGIN SERIALIZER (email / name / phone)
# ----------------------------------------------------------------------
class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField(write_only=True)
    branch_name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    method = serializers.ChoiceField(choices=[('email', 'Email'), ('sms', 'SMS')], write_only=True)

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, data):
        identifier = data.get('identifier')
        branch_name = data.get('branch_name')
        password = data.get('password')

        if not identifier or not branch_name or not password:
            raise serializers.ValidationError("All fields are required.")

        user = None

        # a) Email
        try:
            user = ChurchUser.objects.get(email_address=identifier, branch_name=branch_name)
        except ChurchUser.DoesNotExist:
            pass

        # b) Phone number
        if not user and re.fullmatch(r'[\d+\-\s()]+', identifier):
            try:
                user = ChurchUser.objects.get(phone_number=identifier, branch_name=branch_name)
            except ChurchUser.DoesNotExist:
                pass

        # c) Full name: "First Last" or "First Middle Last"
        if not user and ' ' in identifier.strip():
            parts = identifier.strip().split()
            if len(parts) >= 2:
                first = ' '.join(parts[:-1])
                last = parts[-1]
                try:
                    user = ChurchUser.objects.get(
                        Q(first_name__iexact=first) | Q(first_name__istartswith=first),
                        last_name__iexact=last,
                        branch_name=branch_name
                    )
                except ChurchUser.DoesNotExist:
                    pass

        if not user:
            raise serializers.ValidationError({"non_field_errors": ["Invalid credentials."]})

        if not user.check_password(password):
            raise serializers.ValidationError({"non_field_errors": ["Invalid credentials."]})

        if not user.is_active:
            raise serializers.ValidationError({"non_field_errors": ["Account is disabled."]})

        data['user'] = user
        return data


# ----------------------------------------------------------------------
# 3. OTP REQUEST SERIALIZER
# ----------------------------------------------------------------------
class OTPRequestSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    branch_name = serializers.CharField()
    method = serializers.ChoiceField(choices=[('email', 'Email'), ('sms', 'SMS')])

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, data):
        identifier = data.get('identifier')
        branch_name = data.get('branch_name')

        user = None

        try:
            user = ChurchUser.objects.get(email_address=identifier, branch_name=branch_name)
        except ChurchUser.DoesNotExist:
            pass

        if not user and re.fullmatch(r'[\d+\-\s()]+', identifier):
            try:
                user = ChurchUser.objects.get(phone_number=identifier, branch_name=branch_name)
            except ChurchUser.DoesNotExist:
                pass

        if not user and ' ' in identifier.strip():
            parts = identifier.strip().split()
            if len(parts) >= 2:
                first = ' '.join(parts[:-1])
                last = parts[-1]
                try:
                    user = ChurchUser.objects.get(
                        Q(first_name__iexact=first) | Q(first_name__istartswith=first),
                        last_name__iexact=last,
                        branch_name=branch_name
                    )
                except ChurchUser.DoesNotExist:
                    pass

        if not user:
            raise serializers.ValidationError({"non_field_errors": ["User not found."]})

        data['user'] = user
        return data


# ----------------------------------------------------------------------
# 4. OTP VERIFY SERIALIZER
# ----------------------------------------------------------------------
class OTPVerifySerializer(serializers.Serializer):
    identifier = serializers.CharField(write_only=True)
    branch_name = serializers.CharField(write_only=True)
    otp = serializers.CharField(write_only=True, max_length=6)

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, data):
        identifier = data.get('identifier')
        branch_name = data.get('branch_name')
        otp = data.get('otp')

        if not identifier or not branch_name or not otp:
            raise serializers.ValidationError("All fields are required.")

        user = None

        try:
            user = ChurchUser.objects.get(email_address=identifier, branch_name=branch_name)
        except ChurchUser.DoesNotExist:
            pass

        if not user and re.fullmatch(r'[\d+\-\s()]+', identifier):
            try:
                user = ChurchUser.objects.get(phone_number=identifier, branch_name=branch_name)
            except ChurchUser.DoesNotExist:
                pass

        if not user and ' ' in identifier.strip():
            parts = identifier.strip().split()
            if len(parts) >= 2:
                first = ' '.join(parts[:-1])
                last = parts[-1]
                try:
                    user = ChurchUser.objects.get(
                        Q(first_name__iexact=first) | Q(first_name__istartswith=first),
                        last_name__iexact=last,
                        branch_name=branch_name
                    )
                except ChurchUser.DoesNotExist:
                    pass

        if not user:
            raise serializers.ValidationError({"non_field_errors": ["Invalid credentials."]})

        if user.otp != otp:
            raise serializers.ValidationError({"non_field_errors": ["Invalid OTP."]})

        if user.otp_is_used:
            raise serializers.ValidationError({"non_field_errors": ["OTP already used."]})

        if user.otp_expires_at < timezone.now():
            raise serializers.ValidationError({"non_field_errors": ["OTP has expired."]})

        data['user'] = user
        return data


# ----------------------------------------------------------------------
# 5. PASSWORD RESET SERIALIZER
# ----------------------------------------------------------------------
class PasswordResetRequestSerializer(serializers.Serializer):
    email_address = serializers.EmailField()