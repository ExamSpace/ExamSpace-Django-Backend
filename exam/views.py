from django.shortcuts import render

from .models import Exam, Question, Enrollment
from .serializers import ExamSerializer, QuestionSerializer, EnrollmentSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, CreateAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        is_admin = request.user and request.user.is_superuser
        return request.method in permissions.SAFE_METHODS or is_admin


class ExamsListView(ListCreateAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ExamDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class EnrollMentView(CreateAPIView):
    serializer_class = EnrollmentSerializer

    def perform_create(self, serializer, id=None):
        print(self.kwargs)
        id = self.kwargs.get('id', None)
        exam = Exam.objects.get(pk=id)
        serializer.save(owner=self.request.user, exam=exam)
