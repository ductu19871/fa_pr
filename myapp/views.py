from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
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
            return redirect('otp')
        else:
            error_message = 'Invalid U and P'
    return render(request, 'myapp/login.html', {'error_message': error_message})

# View for the main page
def main_view(request):
    return render(request, 'myapp/main.html')

# View for the OTP page
def otp_view(request):
    return render(request, 'myapp/otp.html')
