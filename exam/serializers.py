from rest_framework import serializers
from .models import Exam, Question, Enrollment, Started, Answered, Cities, Bloodgroup, Countries, Currencies


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        extra_kwargs = {'answer': {'write_only': True}}


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