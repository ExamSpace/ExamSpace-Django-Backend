from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
# Create your models here.

class Countries(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    default_currency = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.title   

class Cities(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    country = models.ForeignKey(to=Countries, on_delete=models.CASCADE, null=True)
    state = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.title

class Bloodgroup(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    blood_group_name = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "Blood Group"    

    def __str__(self):
        return self.blood_group_name
        
class Address(models.Model):
    city = models.ForeignKey(to=Cities, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=191)
    address = models.CharField(max_length=191)
    address_2 = models.CharField(max_length=191)
    zip_code = models.CharField(max_length=191)
    lat = models.CharField(max_length=191)
    long = models.CharField(max_length=191)
    deleted_at = models.DateField(default=date.today)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = "Addresses"


class Configuration(models.Model):
    name = models.CharField(max_length=255)
    organization_name = models.CharField(max_length=255)
    domain_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    meta_title = models.TextField(blank=False)
    meta_desc = models.TextField(blank=False)
    timezone = models.CharField(max_length=100)
    author = models.CharField(max_length=255)
    sms = models.BooleanField(default=False)
    email_notification = models.BooleanField(default=False)
    guest_login = models.BooleanField(default=False)
    front_end = models.BooleanField(default=False)
    slides = models.SmallIntegerField(blank=False)
    translate = models.SmallIntegerField(default=0)
    paid_exam = models.SmallIntegerField(default=1)
    leader_board = models.BooleanField(default=True)
    contact = models.TextField(blank=False)
    photo = models.CharField(max_length=100)
    created_at = models.DateField(default=date.today)
    modified_at = models.DateField(default=date.today)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=5000)
    created_at = models.DateField(default=date.today)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    message = models.TextField()
    status = models.SmallIntegerField(default=0)
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
             

class Currencies(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    sign = models.CharField(max_length=255)
    usd_conversion_amount = models.IntegerField()
    expire_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.title

class Social(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=255)
    social_url = models.CharField(max_length=255)
    social_icon = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Socials"

    def __str__(self):
        return self.social_name            
