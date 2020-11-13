from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

# Create your models here.

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "Please click here to reset your password:" + \
        "http://examspace.ddns.net{}?token={}".format(
            reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset".format(title="ExamSpace"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

    # 'Welcome to ExamSpace!', "Please click on the link to activate your account:"+"http://localhost:8000/api/auth/activate?token="+token
