from django.db import models

class Exam(models.Model):
    title = models.CharField(max_length=250)
    duration= models.FloatField(default=0.0)


class Question(models.Model):
    question = models.CharField(max_length=500)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
