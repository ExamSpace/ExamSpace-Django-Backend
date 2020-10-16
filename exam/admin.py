from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *

admin.site.register(Enrollment)
admin.site.register(Started)
admin.site.register(Exam)
admin.site.register(Answered)
admin.site.register(Subject)
admin.site.register(Mark)

from import_export import resources

class QuestionResource(resources.ModelResource):

    class Meta:
        model = Question

class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource

admin.site.register(Question, QuestionAdmin)