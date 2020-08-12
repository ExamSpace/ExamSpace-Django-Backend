from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
    title = models.CharField(max_length=250)
    duration = models.FloatField(default=0.0)


class Question(models.Model):
    question = models.CharField(max_length=500)
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)


class Enrollment(models.Model):
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
