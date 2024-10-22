import uuid
from typing import Optional

import pyotp
import qrcode
import qrcode.image.svg
from django.conf import settings
from django.db import models
from io import BytesIO


class UserTwoFactorAuthData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="two_factor_auth_data", on_delete=models.CASCADE)

    otp_secret = models.CharField(max_length=255)
    session_identifier = models.UUIDField(blank=True, null=True)

    def generate_qr_code(self, name: Optional[str] = None) -> str:
    # Generate a TOTP object using the OTP secret
        totp = pyotp.TOTP(self.otp_secret, interval=60)
        
        # Generate the provisioning URI for the QR code
        qr_uri = totp.provisioning_uri(name=name, issuer_name="Sonix Example Admin 2FA Demo")
        
        # Create the QR code as an SVG using SvgPathImage
        image_factory = qrcode.image.svg.SvgPathImage
        qr_code_image = qrcode.make(qr_uri, image_factory=image_factory)
        
        # Save the SVG to an in-memory file
        stream = BytesIO()
        qr_code_image.save(stream)
        
        # Get the SVG content as a string
        svg_data = stream.getvalue().decode("utf-8")
        
        # Return the SVG data as a string
        return svg_data

    def validate_otp(self, otp: str) -> bool:
        totp = pyotp.TOTP(self.otp_secret)

        return totp.verify(otp)

    def rotate_session_identifier(self):
        self.session_identifier = uuid.uuid4()

        self.save(update_fields=["session_identifier"])
