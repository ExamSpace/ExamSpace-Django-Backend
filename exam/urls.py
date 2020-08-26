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
    path('config/<int:id>', ConfigurationRetrieveView.as_view()),
    path('config/new', ConfigurationCreateView.as_view()),
    path('config/update/<int:id>', ConfigurationUpdateView.as_view()),
    path('config/delete/<int:id>', ConfigurationDeleteView.as_view()),
    path('contact/<int:id>', ContactRetrieveView.as_view()),
    path('contact/new', ContactCreateView.as_view()),
    path('contact/update/<int:id>', ContactUpdateView.as_view()),
    path('contact/delete/<int:id>', ContactDeleteView.as_view()),
    path('feedback/<int:id>', FeedbackRetrieveView.as_view()),
    path('feedback/new', FeedbackCreateView.as_view()),
    path('feedback/update/<int:id>', FeedbackUpdateView.as_view()),
    path('feedback/delete/<int:id>', FeedbackDeleteView.as_view()),
]
