from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from crum import get_current_user

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
        return str('%s - %s' % (self.name, self.exam))


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
    subject = models.ForeignKey(to=Subject, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return str('%s - %s' % (self.question, self.subject))


class Enrollment(models.Model):
    class Meta:
        unique_together = [['exam', 'owner']]
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(default=timezone.now)


class Started(models.Model):
    class Meta:
        unique_together = [['exam', 'owner']]
        verbose_name_plural = "Started"
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(default=timezone.now)
    ended_at = models.DateTimeField(null=True)
    exam_finished = models.BooleanField(default=False)


class Answered(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)

    class Meta:
        unique_together = [['question', 'user']]
        verbose_name_plural = "Answered"


class Mark(models.Model):
    user = models.ForeignKey(to=User,to_field='username', on_delete=models.CASCADE)
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    total_questions = models.IntegerField(default=0)
    untouched = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    marks_lost =  models.FloatField(default=0.0)
    total =  models.FloatField(default=0.0)
    percentage =  models.FloatField(default=0.0)
    highest_marks =  models.FloatField(default=0.0)
    status =  models.CharField(max_length=255)

    def __str__(self):
        return str('%s - %s - %s - Total Marks: %s' % (self.user, self.exam, self.subject, self.total))