from django.contrib import admin
from .models import *

admin.site.register(Enrollment)
admin.site.register(Started)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answered)
admin.site.register(Subject)
admin.site.register(Mark)

