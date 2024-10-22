import pyotp
from datetime import datetime, timedelta

def send_otp(request, otp_secret_key=None):
    if not otp_secret_key:
        otp_secret_key = pyotp.random_base32()
    totp =  pyotp.TOTP(otp_secret_key, interval=60)
    otp = totp.now()
    request.session['otp_secret_key'] = totp.secret
    valid_date = datetime.now() + timedelta(minutes=1)
    request.session['otp_valid_date'] = str(valid_date)
    print ('your otp', otp)
