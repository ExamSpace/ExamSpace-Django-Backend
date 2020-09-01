from django.shortcuts import render
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

class AddressCreateView(CustomCreateView):
    serializer_class=AddressSerializer
    myClass=Address

class AddressUpdateView(CustomUpdateView):
    serializer_class=AddressSerializer
    myClass=Address  

class AddressRetrieveView(RetrieveAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    lookup_field = "id"


class AddressDeleteView(DestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class ConfigurationCreateView(CustomCreateView):
    serializer_class=ConfigurationSerializer
    myClass=Configuration

class ConfigurationUpdateView(CustomUpdateView):
    serializer_class=ConfigurationSerializer
    myClass=Configuration 

class ConfigurationRetrieveView(RetrieveAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()
    lookup_field = "id"


class ConfigurationDeleteView(DestroyAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class ContactCreateView(CustomCreateView):
    serializer_class=ContactSerializer
    myClass=Contact

class ContactUpdateView(CustomUpdateView):
    serializer_class=ContactSerializer
    myClass=Contact 

class ContactRetrieveView(RetrieveAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = "id"

class ContactDeleteView(DestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class FeedbackCreateView(CustomCreateView):
    serializer_class=FeedbackSerializer
    myClass=Feedback

class FeedbackUpdateView(CustomUpdateView):
    serializer_class=FeedbackSerializer
    myClass=Feedback 

class FeedbackRetrieveView(RetrieveAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    lookup_field = "id"


class FeedbackDeleteView(DestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class CitiesCreateView(CustomCreateView):
    serializer_class=CitiesSerializer
    myClass=Cities

class CitiesUpdateView(CustomUpdateView):
    serializer_class=CitiesSerializer
    myClass=Cities  

class CitiesRetrieveView(RetrieveAPIView):
    serializer_class = CitiesSerializer
    queryset = Cities.objects.all()
    lookup_field = "id"


class CitiesDeleteView(DestroyAPIView):
    serializer_class = CitiesSerializer
    queryset = Cities.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class BloodgroupCreateView(CustomCreateView):
    serializer_class=BloodgroupSerializer
    myClass=Bloodgroup

class BloodgroupUpdateView(CustomUpdateView):
    serializer_class=BloodgroupSerializer
    myClass=Bloodgroup  

class BloodgroupRetrieveView(RetrieveAPIView):
    serializer_class = BloodgroupSerializer
    queryset = Bloodgroup.objects.all()
    lookup_field = "id"


class BloodgroupDeleteView(DestroyAPIView):
    serializer_class = BloodgroupSerializer
    queryset = Bloodgroup.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class CountriesCreateView(CustomCreateView):
    serializer_class=CountriesSerializer
    myClass=Countries

class CountriesUpdateView(CustomUpdateView):
    serializer_class=CountriesSerializer
    myClass=Countries  

class CountriesRetrieveView(RetrieveAPIView):
    serializer_class = CountriesSerializer
    queryset = Countries.objects.all()
    lookup_field = "id"


class CountriesDeleteView(DestroyAPIView):
    serializer_class = CountriesSerializer
    queryset = Countries.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class CurrenciesCreateView(CustomCreateView):
    serializer_class=CurrenciesSerializer
    myClass=Currencies

class CurrenciesUpdateView(CustomUpdateView):
    serializer_class=CurrenciesSerializer
    myClass=Currencies  

class CurrenciesRetrieveView(RetrieveAPIView):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()
    lookup_field = "id"


class CurrenciesDeleteView(DestroyAPIView):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class SocialCreateView(CustomCreateView):
    serializer_class=SocialSerializer
    myClass=Social

class SocialUpdateView(CustomUpdateView):
    serializer_class=SocialSerializer
    myClass=Social  

class SocialRetrieveView(RetrieveAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()
    lookup_field = "id"


class SocialDeleteView(DestroyAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )
