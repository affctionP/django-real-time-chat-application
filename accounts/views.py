from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.utils import timezone
from .models import OTPCode, User
from .utils import generate_otp_code, send_otp_email

def request_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            otp_code = generate_otp_code()
            OTPCode.objects.create(user=user, code=otp_code)
            send_otp_email(user, otp_code)
            return redirect('verify_otp')  # Redirect to OTP verification page
        except User.DoesNotExist:
            return render(request, 'request_otp.html', {'error': 'User with this email does not exist.'})
    return render(request, 'request_otp.html')

def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp_code = request.POST.get('otp_code')
        try:
            user = User.objects.get(email=email)
            otp = OTPCode.objects.filter(user=user, code=otp_code).first()
            if otp and otp.is_valid():
                login(request, user)
                return redirect('home')  # Redirect to homepage or dashboard
            else:
                return render(request, 'verify_otp.html', {'error': 'Invalid or expired OTP code.'})
        except User.DoesNotExist:
            return render(request, 'verify_otp.html', {'error': 'User with this email does not exist.'})
    return render(request, 'verify_otp.html')