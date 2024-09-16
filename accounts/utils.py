import random
import string
from django.core.mail import send_mail
from django.conf import settings
def generate_otp_code():
    return ''.join(random.choices(string.digits, k=6))

def send_otp_email(user, otp_code):
    subject = 'Your OTP Code'
    message = f'Hello {user.name},\n\nYour OTP code is: {otp_code}\nIt is valid for 5 minutes.'
    from_email = 'roshanadadegostar@gmail.com'  # Update with your email address
    recipient_list = [user.email]
    send_mail(subject, message,settings.DEFAULT_FROM_EMAIL, recipient_list)