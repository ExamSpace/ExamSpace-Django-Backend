from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

EXAM_TYPE = (
    ('marathon', 'MARATHON'),
    ('single', 'SINGLE'),
    ('timer', 'TIMER'),
)


class Exam(models.Model):
    name = models.CharField(max_length=255)
    instruction = models.TextField()
    duration = models.IntegerField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    passing_percent = models.IntegerField()
    negative_marking = models.BooleanField(default=False)
    negative_marks = models.FloatField(default=0.0)
    marks = models.FloatField()
    ques_random = models.BooleanField(default=False)
    paid_exam = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=4, default=0.0)
    status = models.CharField(max_length=10, blank=True)
    finalized_time = models.DateField(default=timezone.now)
    created = models.DateField(default=timezone.now)
    modified = models.DateField(default=timezone.now)
    examtype = models.CharField(
        max_length=50, choices=EXAM_TYPE, default='marathon')
    title_image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    img = models.URLField(blank=True)
    question = models.TextField(blank=False)
    option1 = models.TextField(blank=True)
    option2 = models.TextField(blank=True)
    option3 = models.TextField(blank=True)
    option4 = models.TextField(blank=True)
    option5 = models.TextField(blank=True)
    option6 = models.TextField(blank=True)
    marks = models.FloatField(default=1.0)
    hint = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    explort = models.TextField(blank=True)
    answer = models.IntegerField(blank=False)
    true_false = models.BooleanField(default=False)
    fill_blank = models.BooleanField(default=False)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Enrollment(models.Model):
    class Meta:
        unique_together = [['exam', 'owner']]
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(default=timezone.now)


class Started(models.Model):
    class Meta:
        unique_together = [['exam', 'owner']]
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Started"


class Answered(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0, unique=True)

    class Meta:
        verbose_name_plural = "Answered"

class Address(models.Model):
    city_id = models.IntegerField(blank=False)
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

class Cities(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    country_id = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    created = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)

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

class Countries(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    default_currency = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.title        

class Currencies(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    sign = models.CharField(max_length=255)
    usd_conversion_amount = models.IntegerField()
    expire_at = models.DateField(default=date.today)

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.title
       