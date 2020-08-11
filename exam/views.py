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

    def post(self, request, id=None):
        user = request.user
        exam = Exam.objects.get(pk=id)

        serializer = EnrollmentSerializer(owner=user, exam=exam)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        