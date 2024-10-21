import pyotp
from django.core.exceptions import ValidationError

# from styleguide_example.users.models import BaseUser

from .models import UserTwoFactorAuthData


def user_two_factor_auth_data_create(user):
    # Check if user already has 2FA data
    if UserTwoFactorAuthData.objects.filter(user=user).exists():
        # raise ValidationError("User already has 2FA data.")
        return UserTwoFactorAuthData.objects.filter(user=user).last()

    # Create a new 2FA data object if it doesn't exist
    otp_secret = pyotp.random_base32()  # Generate a random OTP secret
    two_factor_auth_data, created = UserTwoFactorAuthData.objects.get_or_create(
        user=user,
        defaults={'otp_secret': otp_secret}
    )

    if not created:
        raise ValidationError("Failed to create 2FA data. The user may already have it.")