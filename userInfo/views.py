from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from .CustomViews import *

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        is_admin = request.user and request.user.is_superuser
        return request.method in permissions.SAFE_METHODS or is_admin

class ProfileCreateUpdateView(CustomCreateUpdateView):
    serializer_class=ProfileSerializer
    myClass=Profile

class ProfileRetrieveView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class ProfileDeleteView(DestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class ConfigurationCreateUpdateView(CustomCreateUpdateView):
    serializer_class=ConfigurationSerializer
    myClass=Configuration

class ConfigurationRetrieveView(RetrieveAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class ConfigurationDeleteView(DestroyAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class ContactCreateUpdateView(CustomCreateUpdateView):
    serializer_class=ContactSerializer
    myClass=Contact


class ContactRetrieveView(RetrieveAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

class ContactDeleteView(DestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class FeedbackCreateUpdateView(CustomCreateUpdateView):
    serializer_class=FeedbackSerializer
    myClass=Feedback

class FeedbackRetrieveView(RetrieveAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class FeedbackDeleteView(DestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class CitiesCreateUpdateView(CustomCreateUpdateView):
    serializer_class=CitiesSerializer
    myClass=Cities


class CitiesRetrieveView(ListAPIView):
    serializer_class = CitiesSerializer
    queryset = Cities.objects.all()


class CitiesDeleteView(DestroyAPIView):
    serializer_class = CitiesSerializer
    queryset = Cities.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class CountriesCreateUpdateView(CustomCreateUpdateView):
    serializer_class=CountriesSerializer
    myClass=Countries


class CountriesRetrieveView(RetrieveAPIView):
    serializer_class = CountriesSerializer
    queryset = Countries.objects.all()
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class CountriesDeleteView(DestroyAPIView):
    serializer_class = CountriesSerializer
    queryset = Countries.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class CurrenciesCreateUpdateView(CustomCreateUpdateView):
    serializer_class=CurrenciesSerializer
    myClass=Currencies


class CurrenciesRetrieveView(RetrieveAPIView):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class CurrenciesDeleteView(DestroyAPIView):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class SocialCreateUpdateView(CustomCreateUpdateView):
    serializer_class=SocialSerializer
    myClass=Social

class SocialRetrieveView(RetrieveAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class SocialDeleteView(DestroyAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )
