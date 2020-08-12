from django.urls import path
from .views import ExamsListView, ExamDetailView, EnrollMentView

urlpatterns = [
    path('list', ExamsListView.as_view()),
    path('<int:id>', ExamDetailView.as_view()),
    path('<int:exam_id>/questionList', QuestionsListView.as_view()),
    path('<int:exam_id>/Question', QuestionDetailView.as_view()),
    path('<int:id>/enroll', EnrollMentView.as_view()),
]
