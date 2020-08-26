from django.contrib import admin
from .models import Enrollment, Question, Exam, Started, Answered, Subject,Address, Cities, Bloodgroup, Countries, Currencies

admin.site.register(Enrollment)
admin.site.register(Started)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answered)
admin.site.register(Subject)
admin.site.register(Address)
admin.site.register(Cities)
admin.site.register(Bloodgroup)
admin.site.register(Countries)
admin.site.register(Currencies)
# Register your models here.
