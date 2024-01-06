from django.core.mail import send_mail
import uuid
from django.conf import settings


def send_forget_password_mail(email,token):
    subject = 'your forget password link'
    Message  = f'Hi click here the link  to rest a password http://127.0.0.1:8000/ChangePassword/{token}/'
    email_form  = settings.EMAIL_HOST_USER
    recipient_list =[email]
    send_mail(subject,Message,email_form,recipient_list)
    return True


def send_email_token(email,token):
    try:
        subject = 'Welcome to Bizvility please verified  your account'
        Message  = f'Hi click here the link  to Verify http://127.0.0.1:8000/verify/{token}/'
        email_form  = settings.EMAIL_HOST_USER
        recipient_list =[email]
        send_mail(subject,Message,email_form,recipient_list)
    except Exception as e:
        return False

    return True