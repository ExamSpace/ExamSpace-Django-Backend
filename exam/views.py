from django.shortcuts import render

from .models import Exam, Question
from .serializers import ExamSerializer, QuestionSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions


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
