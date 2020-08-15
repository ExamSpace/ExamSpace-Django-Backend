from django.urls import path
from .views import ExamsListView, ExamDetailView, EnrollMentView, QuestionsListView, QuestionDetailView, StartedView, AnsweredView

urlpatterns = [
    path('list', ExamsListView.as_view()),
    path('<int:id>', ExamDetailView.as_view()),
    path('<int:examId>/questionList', QuestionsListView.as_view()),
    path('<int:examId>/question/<int:id>', QuestionDetailView.as_view()),
    path('<int:id>/start', StartedView.as_view()),
    path('<int:id>/enroll', EnrollMentView.as_view()),
    path('<int:examId>/question/<int:qid>/answer/selected_option=<int:option>', AnsweredView.as_view()),
]
