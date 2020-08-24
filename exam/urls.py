from django.urls import path
from .views import ExamsListView, ExamDetailView, EnrollMentView, QuestionsListView, QuestionDetailView, StartedView, AnsweredView, CitiesListView, CitiesDetailView, BloodgroupListView, BloodgroupDetailView, CountriesListView, CountriesDetailView, CurrenciesListView, CurrenciesDetailView

urlpatterns = [
    path('list', ExamsListView.as_view()),
    path('<int:id>', ExamDetailView.as_view()),
    path('<int:examId>/questionList', QuestionsListView.as_view()),
    path('<int:examId>/question/<int:id>', QuestionDetailView.as_view()),
    path('<int:id>/start', StartedView.as_view()),
    path('<int:id>/enroll', EnrollMentView.as_view()),
    path('<int:examId>/question/<int:qid>/answer/selected_option=<int:option>', AnsweredView.as_view()),
    path('cities', CitiesListView.as_view()),
    path('cities/<int:id>', CitiesDetailView.as_view()),
    path('bloodgroup', BloodgroupListView.as_view()),
    path('bloodgroup/<int:id>', BloodgroupDetailView.as_view()),
    path('countries', CountriesListView.as_view()),
    path('countries/<int:id>', CountriesDetailView.as_view()),
    path('currencies', CurrenciesListView.as_view()),
    path('currencies/<int:id>', CurrenciesDetailView.as_view()),        
]
