from django.urls import path
from .views import *

urlpatterns = [
    path('list', ExamsListView.as_view()),
    path('<int:id>', ExamDetailView.as_view()),
    path('new', ExamCreateView.as_view()),
    path('subjectList', SubjectsView.as_view()),
    path('<int:examId>/subjectList', SubjectsListView.as_view()),
    path('<int:examId>/subject/<int:id>', SubjectDetailView.as_view()),
    path('<int:examId>/subject/new', SubjectCreateView.as_view()),
    path('<int:examId>/questionList',
         QuestionsPerExam.as_view()),
    path('<int:examId>/subject/<int:subjectId>/questionList',
         QuestionsListView.as_view()),
    path('<int:examId>/subject/<int:subjectId>/question/<int:id>',
         QuestionDetailView.as_view()),
    path('<int:examId>/subject/<int:subjectId>/question/new',
         QuestionCreateView.as_view()),
    path('<int:id>/start', StartedView.as_view()),
    path('<int:id>/stop', EndedExamView.as_view()),
    path('<int:id>/enroll', EnrollMentView.as_view()),
    path('<int:examId>/question/<int:qid>/answer/selected_option=<int:option>',
         AnsweredView.as_view()),
    path('<int:examId>/submit_answer_list', AnsweredListVew.as_view()),
    path('<int:examId>/question/<int:qid>/answer/selected_option=<int:option>',
         AnsweredView.as_view()),
    path('<int:examId>/marksList', MarksListView.as_view()),
    path('<int:examId>/mark/<int:id>', MarkDetailView.as_view()),
    path('<int:examId>/mark/new', MarkCreateView.as_view()),

]
