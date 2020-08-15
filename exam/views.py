from django.shortcuts import render

from .models import Exam, Question, Enrollment, Answered
from .serializers import ExamSerializer, QuestionSerializer, EnrollmentSerializer, StartedSerializer, AnsweredSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, CreateAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        is_admin = request.user and request.user.is_superuser
        return request.method in permissions.SAFE_METHODS or is_admin


class ExamsListView(ListCreateAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ExamDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    lookup_field = "id"
    # permission_classes = (IsAdminOrReadOnly, )


class QuestionsListView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        examId=self.kwargs['examId']
        return Question.objects.filter(exam=examId)  
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    

class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer   
    def get_queryset(self):
        examId=self.kwargs['examId']
        return Question.objects.filter(exam=examId)
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class EnrollMentView(CreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer, id=None):
        print(self.kwargs)
        id = self.kwargs.get('id', None)

        try:
            exam = Exam.objects.get(pk=id)
            serializer.save(owner=self.request.user, exam=exam)
        except ObjectDoesNotExist as identifier:
            return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)

class StartedView(CreateAPIView):
    serializer_class = StartedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer, id=None):
        print(self.kwargs)
        id = self.kwargs.get('id', None)

        try:
            exam = Exam.objects.get(pk=id)
            serializer.save(owner=self.request.user, exam=exam)
        except ObjectDoesNotExist as identifier:
            return Response('Bad request', status=status.HTTP_400_BAD_REQUEST) 

class AnsweredView(CreateAPIView):
    serializer_class = AnsweredSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qid=self.kwargs['qid']
        return Question.objects.filter(Question=qid)                       
