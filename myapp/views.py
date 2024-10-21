from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .utils import send_otp
import pyotp
from django.contrib.auth.models import User
# View for the login page
def login_view(request):
    print ('**ldfjdlkf')
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['username'] = username
            send_otp(request)
            return redirect('otp')
        else:
            error_message = 'Invalid U and P'
    return render(request, 'myapp/login.html', {'error_message': error_message})

# View for the main page
@login_required
def main_view(request):
    return render(request, 'myapp/main.html')

def logout_view(request):
    logout(request)
    return redirect('login')



# View for the OTP page
def otp_view(request):
    error_message = None
    if request.method == 'POST':
        otp = request.POST['otp']
        username = request.session['username']
        otp_secret_key = request.session['otp_secret_key']
        valid_date = request.session['otp_valid_date']
        if otp_secret_key:
            totp =  pyotp.TOTP(otp_secret_key, interval=60)
            if totp.verify(otp):
                user = get_object_or_404(User, username=username)
                login(request, user)
                del request.session['otp_secret_key']
                del request.session['otp_valid_date']
                return redirect('main')
    return render(request, 'myapp/otp.html')
