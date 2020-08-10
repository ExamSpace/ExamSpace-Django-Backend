from django.urls import path
from .views import LoginView, RefreshView, RegistrationView, ActivateView, LogoutView, ForgetPasswordEmailView, ResetPasswordView
from .views import UserInfo
urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegistrationView.as_view()),
    path('activate', ActivateView.as_view()),
    path('refresh', RefreshView.as_view()),
    path('logout', LogoutView.as_view()),
    path('forget/email', ForgetPasswordEmailView.as_view()),
    path('reset/password', ResetPasswordView.as_view()),
    path('userinfo', UserInfo.as_view()),
]
