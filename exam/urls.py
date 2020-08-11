from django.urls import path
from .views import ExamsListView

urlpatterns = [
    path('list', ExamsListView.as_view()),
]
