from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.conf import settings
import jwt
from django.contrib import auth
from .serializers import UserSerializer, LoginSerializer, RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.core.cache import cache
import uuid
from django.core.mail import send_mail
from django.conf import settings
from asgiref.sync import async_to_sync
from django.shortcuts import redirect
from rest_framework import generics
from . import serializers
from rest_framework.permissions import IsAuthenticated
from .serializers import ChangePasswordSerializer  


@async_to_sync
async def mailSender(subject, message, recipient_list):
    send_mail(subject=subject, message=message,
              recipient_list=recipient_list, from_email=settings.EMAIL_HOST_USER, fail_silently=True)

class RegistrationView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            user.is_active = False
            user.save()

            token = jwt.encode(
                {'username': serializer.data['username'], 'exp': datetime.utcnow()+timedelta(minutes=60)}, settings.JWT_SECRET_KEY).decode('utf-8')

            async_to_sync(mailSender('Welcome to ExamSpace!', "Please click on the link to activate your account:"+"http://examspace.ddns.net:8000/api/auth/activate?token="+token,
                                     [serializer.data['email']]), force_new_loop=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateView(APIView):
    def get(self, request, format=None):
        token = request.GET.get('token', ' ')
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
            username = payload["username"]
            user = User.objects.get(username=username)
            if user:
                user.is_active = True
                user.save()
                return redirect('http://examspace.ddns.net/')
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(detail='Invalid token')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(detail='Invalid token')


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if user:
            auth_token = jwt.encode(
                {'username': user.username, 'exp': datetime.utcnow()+timedelta(minutes=100)}, settings.JWT_SECRET_KEY)

            uinque_id = uuid.uuid1().hex
            refresh_token = jwt.encode(
                {'username': user.username, 'id': uinque_id, 'exp': datetime.utcnow(
                ) + timedelta(days=1), }, settings.JWT_SECRET_KEY
            )

            serializer = UserSerializer(user)
            data = {'user': serializer.data,
                    'token': auth_token}

            # Cache the refresh token
            cache.set(username+uinque_id, refresh_token.decode("utf-8"), timeout=timedelta(
                days=1).total_seconds())
            # Caching complete

            response = Response(data, status=status.HTTP_200_OK)
            response.set_cookie(
                'refresh', refresh_token.decode('utf-8'), max_age=timedelta(days=1).total_seconds(), samesite='Lax')
            return response
        return Response({'detail': 'Username or Password incorrect'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def get(self, request, format=None):
        auth_data = request.COOKIES.get('refresh', '')
        if not auth_data:
            return Response({'detail': 'Empty token'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            payload = jwt.decode(auth_data, settings.JWT_SECRET_KEY)
            cache.expire(payload["username"] +
                         payload.get('id'), timeout=0)
            response = Response({'detail': 'Logged Out'},
                                status=status.HTTP_200_OK)
            response.delete_cookie('refresh')
            return response
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(detail='Invalid token')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(detail='Invalid token')


class RefreshView(APIView):
    def get(self, request, format=None):
        auth_data = request.COOKIES.get('refresh', '')
        if not auth_data:
            return Response({'detail': 'Empty token'}, status=status.HTTP_400_BAD_REQUEST)

        token = auth_data
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)

            # Look into cache
            ok = cache.get(payload["username"]+payload["id"])
            if not ok:
                return Response({'detail': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
            # Lookout complete

            user = User.objects.get(username=payload['username'])

            if user:
                auth_token = jwt.encode(
                    {'username': user.username, 'exp': datetime.utcnow() + timedelta(minutes=5)}, settings.JWT_SECRET_KEY)

                uinque_id = uuid.uuid1().hex
                refresh_token = jwt.encode(
                    {'username': user.username, 'id': uinque_id, 'exp': datetime.utcnow(
                    ) + timedelta(days=1)}, settings.JWT_SECRET_KEY
                )

                data = {'token': auth_token}

                # Remove prev token from cache
                cache.expire(user.username+payload["id"], timeout=0)
                # Insert new refresh token to cache
                cache.set(user.username + uinque_id, refresh_token.decode("utf-8"),
                          timeout=timedelta(days=1).total_seconds())
                # Caching Complete

                response = Response(data, status=status.HTTP_200_OK)
                response.set_cookie(
                    'refresh', refresh_token.decode('utf-8'), max_age=timedelta(days=1).total_seconds(), samesite='Lax')
                return response

            return Response({'detail': 'Invalid cradential'}, status=status.HTTP_401_UNAUTHORIZED)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(detail='Invalid token')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(detail='Invalid token')


class ForgetPasswordEmailView(APIView):
    def post(self, request, format=None):
        data = request.data
        email = data.get('email', ' ')
        user = User.objects.get(email=email)
        if user:
            token = jwt.encode(
                {'email': email, 'exp': datetime.utcnow() + timedelta(minutes=60)}, settings.JWT_SECRET_KEY).decode('utf-8')
            cache.set(email+"_pass_reset_token", token,
                      timeout=timedelta(minutes=60).total_seconds())
            return Response({'token': token}, status=status.HTTP_200_OK)
        return Response({'detail': 'No account found with this email'}, status=status.HTTP_401_UNAUTHORIZED)


class ResetPasswordView(APIView):
    def post(self, request, format=None):
        token = request.GET.get('token', '')
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
            email = payload['email']

            chached_token = cache.get(email + "_pass_reset_token")

            if not chached_token or token != chached_token:
                return Response({'detail': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

            data = request.data
            password = data.get('password', ' ')

            if password.__len__() < 5:
                return Response({'detail': 'Password too short'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()

            cache.expire(email + "_pass_reset_token", timeout=0)

            return Response({'detail': 'Password successfully changed'}, status=status.HTTP_200_OK)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(detail='Invalid token')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(detail='Invalid token')


class UserInfo(APIView):
    def get(self, request, format=None):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return Response({'detail': 'Empty token'}, status=status.HTTP_400_BAD_REQUEST)

        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
            user = User.objects.get(username=payload['username'])
            if user:
                serializer = UserSerializer(user)
                data = {'user': serializer.data}
                return Response(data, status=status.HTTP_200_OK)
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(detail='Invalid token')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(detail='Invalid token')

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)