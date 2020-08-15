from django.contrib import admin
from .models import Enrollment, Question, Exam, Started, Answered

admin.site.register(Enrollment)
admin.site.register(Started)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answered)
# Register your models here.
