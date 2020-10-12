from rest_framework import serializers
from .models import *
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        # extra_kwargs = {'answer': {'write_only': True}}


class SubjectSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['name', 'exam', 'questions']


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = []


class StartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Started
        fields = []


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        extra_kwargs = {'answer': {'write_only': True}}


class StartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Started
        fields = []


class AnsweredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answered
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

    def validate(self, data):
        question = data['question']
        if Answered.objects.filter(user=self.context["request"].user, question=question).exists():
            raise serializers.ValidationError(
                "You have already answered this question")
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        obj = Answered.objects.create(**validated_data, user=user)
        obj.save()
        return obj


class CorrectAnswerField(serializers.RelatedField):
    def to_representation(self, value):
        return '%d' % (value.answer)


class AnsweredWithCorrectAnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all())
    correct_answer = serializers.IntegerField(
        source='question.answer', read_only=True)

    class Meta:
        model = Answered
        fields = ['question', 'correct_answer', 'answer']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'
