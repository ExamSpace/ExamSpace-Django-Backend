from django.contrib import admin
from .models import Enrollment, Question, Exam

admin.site.register(Enrollment)
admin.site.register(Exam)
admin.site.register(Question)
# Register your models here.
