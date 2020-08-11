from django.urls import path
from .views import ExamsListView, ExamDetailView

urlpatterns = [
    path('list', ExamsListView.as_view()),
    path('<int:id>', ExamDetailView.as_view()),
]
