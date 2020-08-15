from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Exam(models.Model):
    name = models.CharField(max_length=255)
    instruction = models.TextField()
    duration = models.IntegerField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    passing_percent = models.IntegerField()
    negative_marking = models.CharField(max_length=3)
    negative_marks = models.FloatField()
    marks = models.FloatField()
    attempt_count = models.IntegerField()
    declare_result = models.CharField(max_length=3)
    finish_result = models.CharField(max_length=1)
    ques_random = models.CharField(max_length=1)
    paid_exam = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=10, decimal_places=0, )
    status = models.CharField(max_length=10)
    user_id = models.IntegerField()
    finalized_time = models.DateField(default=timezone.now)
    created = models.DateField(default=timezone.now)
    modified = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name


class Question(models.Model):
    qtype_id = models.IntegerField()
    img = models.CharField(max_length=200)
    qtag_id = models.IntegerField()
    question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    option5 = models.TextField()
    option6 = models.TextField()
    marks = models.FloatField()
    negative_marks = models.FloatField()
    hint = models.TextField()
    explanation = models.TextField()
    explort = models.TextField()
    answer = models.CharField(max_length=15)
    true_false = models.CharField(max_length=5)
    fill_blank = models.CharField(max_length=100)
    status = models.CharField(max_length=3)
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    def __str__(self):
        return self.question


class Enrollment(models.Model):
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(default=timezone.now)


class Started(models.Model):
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name_plural = "Started"


class Answered(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Answered"


    