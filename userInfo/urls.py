from django.urls import path
from .views import *

urlpatterns = [
    path('profile', ProfileRetrieveView.as_view()),
    path('profile/new', ProfileCreateUpdateView.as_view()),
    path('config', ConfigurationRetrieveView.as_view()),
    path('config/new', ConfigurationCreateUpdateView.as_view()),
    path('contact', ContactRetrieveView.as_view()),
    path('contact/new', ContactCreateUpdateView.as_view()),
    path('feedback', FeedbackRetrieveView.as_view()),
    path('feedback/new', FeedbackCreateUpdateView.as_view()),
    path('cities', CitiesRetrieveView.as_view()),
    path('cities/new', CitiesCreateUpdateView.as_view()),  
    path('countries', CountriesRetrieveView.as_view()),
    path('countries/new', CountriesCreateUpdateView.as_view()),
    path('currencies', CurrenciesRetrieveView.as_view()),
    path('currencies/new', CurrenciesCreateUpdateView.as_view()),
    path('social', SocialRetrieveView.as_view()),
    path('social/new', SocialCreateUpdateView.as_view()),
  
]

