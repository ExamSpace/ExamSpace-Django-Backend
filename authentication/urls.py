from django.urls import path
from .views import LoginView, RefreshView, RegistrationView, ActivateView, LogoutView, ForgetPasswordEmailView, ResetPasswordView, ChangePasswordView
from .views import UserInfo
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),    
    # path('login', LoginView.as_view()),
    path('register', RegistrationView.as_view()),
    path('activate', ActivateView.as_view()),
    path('refresh', RefreshView.as_view()),
    path('logout', LogoutView.as_view()),
    # path('forget/email', ForgetPasswordEmailView.as_view()),
    # path('reset/password', ResetPasswordView.as_view()),
    path('userinfo', UserInfo.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]
