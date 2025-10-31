# authentication/views.py
from django.contrib.auth import login
from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from datetime import timedelta
import random

from .models import ChurchUser
from .serializers import (
    UserSignupSerializer, LoginSerializer, OTPRequestSerializer,
    OTPVerifySerializer, PasswordResetRequestSerializer
)

# -------------------------------------------------------------------------
# EMAIL HELPERS
# -------------------------------------------------------------------------
CHURCH_NAME = "Royal Gospel Church Int."

def send_welcome_email(user):
    subject = f"Welcome to {CHURCH_NAME}, {user.first_name}!"
    message = (
        f"Hello {user.get_full_name()},\n\n"
        f"Welcome to {CHURCH_NAME}! We're excited to have you as part of our family.\n\n"
        f"Branch: {user.branch_name}\n"
        f"Role: {user.get_role_display()}\n\n"
        f"You can now log in using your email and password.\n\n"
        f"God bless you!\n"
        f"{CHURCH_NAME} Media Team"
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email_address], fail_silently=False)

def send_login_success_email(user):
    subject = f"Login Successful – {CHURCH_NAME}"
    message = (
        f"Hello {user.get_full_name()},\n\n"
        f"You have successfully logged in to your {CHURCH_NAME} account.\n\n"
        f"Time: {timezone.localtime().strftime('%Y-%m-%d %I:%M %p')}\n"
        f"Branch: {user.branch_name}\n\n"
        f"If this wasn't you, please contact the church admin immediately.\n\n"
        f"Stay blessed!\n"
        f"{CHURCH_NAME} Media Team"
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email_address], fail_silently=False)

def send_otp_email(user, otp):
    subject = f"Your {CHURCH_NAME} Login OTP"
    message = (
        f"Hello {user.get_full_name()},\n\n"
        f"Your One-Time Password (OTP) is:\n"
        f"{otp}\n\n"
        f"This code expires in 5 minutes.\n"
        f"Use it to complete your login.\n\n"
        f"God bless you!\n"
        f"{CHURCH_NAME} Media Team"
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email_address], fail_silently=False)

def send_otp_sms(user, otp):
    print(f"[SMS] To {user.phone_number}: Your OTP is {otp}")

# -------------------------------------------------------------------------
# API VIEWS
# -------------------------------------------------------------------------
class SignupView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_welcome_email(user)
            return Response({"message": "User registered successfully. Welcome email sent!", "user_id": user.id}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            method = serializer.validated_data['method']
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            expires_at = timezone.now() + timedelta(minutes=5)
            user.otp = otp
            user.otp_method = method
            user.otp_created_at = timezone.now()
            user.otp_expires_at = expires_at
            user.otp_is_used = False
            user.save()
            if method == 'email':
                send_otp_email(user, otp)
            else:
                send_otp_sms(user, otp)
            return Response({"message": f"OTP sent via {method}.", "user_id": user.id, "method": method})
        return Response(serializer.errors, status=400)

class OTPRequestView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            method = serializer.validated_data['method']
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            expires_at = timezone.now() + timedelta(minutes=5)
            user.otp = otp
            user.otp_method = method
            user.otp_created_at = timezone.now()
            user.otp_expires_at = expires_at
            user.otp_is_used = False
            user.save()
            if method == 'email':
                send_otp_email(user, otp)
            else:
                send_otp_sms(user, otp)
            return Response({"message": f"OTP sent via {method}."})
        return Response(serializer.errors, status=400)

class OTPVerifyView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user.otp_is_used = True
            user.save()
            login(request, user)
            send_login_success_email(user)
            return Response({
                "message": "Login successful. Confirmation email sent!",
                "user": {
                    "id": user.id,
                    "full_name": user.get_full_name(),
                    "email": user.email_address,
                    "role": user.role,
                    "branch": user.branch_name
                }
            })
        return Response(serializer.errors, status=400)


# -------------------------------------------------------------------------
# PASSWORD RESET (100% API – NO TEMPLATES)
# -------------------------------------------------------------------------
class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email_address']
            user = ChurchUser.objects.get(email_address=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(
                reverse('password-reset-confirm-api')
            ) + f"?uid={uid}&token={token}"
            send_mail(
                "Password Reset Request",
                f"Use this link to reset your password:\n\n{reset_url}\n\n"
                f"Or use the API directly with uid and token.",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return Response({"message": "Password reset link sent."})
        return Response(serializer.errors, status=400)


class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        uid = request.data.get('uid')
        token = request.data.get('token')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if not all([uid, token, new_password, confirm_password]):
            return Response({"error": "All fields are required."}, status=400)

        if new_password != confirm_password:
            return Response({"error": "Passwords do not match."}, status=400)

        if len(new_password) < 8:
            return Response({"error": "Password must be at least 8 characters."}, status=400)

        try:
            uid_int = urlsafe_base64_decode(uid).decode()
            user = ChurchUser.objects.get(pk=uid_int)
        except (TypeError, ValueError, OverflowError, ChurchUser.DoesNotExist):
            return Response({"error": "Invalid reset link."}, status=400)

        if not default_token_generator.check_token(user, token):
            return Response({"error": "Invalid or expired token."}, status=400)

        user.set_password(new_password)
        user.save()
        return Response({"message": "Password changed successfully! You can now log in."})