from rest_framework import serializers
from .models import Exam, Question, Enrollment, Started, Answered, Subject,Address, Cities, Bloodgroup, Countries, Currencies


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = []

class StartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Started
        fields = []

class AnsweredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answered
        fields = []                      

    # def save(self):
     #   return super

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
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
