from rest_framework import serializers
from .models import Exam, Question, Enrollment, Started, Answered


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
