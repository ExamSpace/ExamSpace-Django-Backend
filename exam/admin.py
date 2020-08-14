from django.contrib import admin
from .models import Enrollment, Question, Exam, Started

admin.site.register(Enrollment)
admin.site.register(Started)
admin.site.register(Exam)
admin.site.register(Question)
# Register your models here.
