from rest_framework import serializers
from .models import *
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'   

class BloodgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloodgroup
        fields = '__all__' 

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'                   
class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'                  
