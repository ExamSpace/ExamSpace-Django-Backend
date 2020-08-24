from django.contrib import admin
from .models import Enrollment, Question, Exam, Started, Answered, Subject,Address

admin.site.register(Enrollment)
admin.site.register(Started)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answered)
admin.site.register(Subject)
admin.site.register(Address)
# Register your models here.
