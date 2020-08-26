from django.urls import path
# from .views import ExamsListView, ExamDetailView, EnrollMentView, QuestionsListView, QuestionDetailView, StartedView, AnsweredView, SubjectListView
from .views import *

urlpatterns = [
    path('list', ExamsListView.as_view()),
    path('<int:id>', ExamDetailView.as_view()),
    path('new', ExamCreateView.as_view()),
    path('<int:examId>/subjectList', SubjectsListView.as_view()),
    path('<int:examId>/subject/<int:id>', SubjectDetailView.as_view()),
    path('<int:examId>/subject/new', SubjectCreateView.as_view()),
    path('<int:examId>/subject/<int:subjectId>/questionList', QuestionsListView.as_view()),
    path('<int:examId>/subject/<int:subjectId>/question/<int:id>', QuestionDetailView.as_view()),
    path('<int:examId>/subject/<int:subjectId>/question/new', QuestionCreateView.as_view()),
    path('<int:id>/start', StartedView.as_view()),
    path('<int:id>/enroll', EnrollMentView.as_view()),
    path('<int:examId>/<int:subjectId>/question/<int:qid>/answer/selected_option=<int:option>', AnsweredView.as_view()),
    path('address/<int:id>', AddressRetrieveView.as_view()),
    path('address/new', AddressCreateView.as_view()),
    path('address/update/<int:id>', AddressUpdateView.as_view()),
    path('address/delete/<int:id>', AddressDeleteView.as_view()),
    
    
]
