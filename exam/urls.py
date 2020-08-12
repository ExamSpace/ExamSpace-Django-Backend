from django.urls import path
from .views import ExamsListView, ExamDetailView, EnrollMentView, QuestionsListView, QuestionDetailView

urlpatterns = [
    path('list', ExamsListView.as_view()),
    path('<int:id>', ExamDetailView.as_view()),
    path('<int:examId>/questionList', QuestionsListView.as_view()),
    path('<int:examId>/Question/<int:id>', QuestionDetailView.as_view()),
    path('<int:id>/enroll', EnrollMentView.as_view()),
]
