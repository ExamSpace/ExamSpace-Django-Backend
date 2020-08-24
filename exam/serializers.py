from rest_framework import serializers
from .models import Exam, Question, Enrollment, Started, Answered, Subject,Address


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
