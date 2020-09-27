from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework.views import APIView



class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        is_admin = request.user and request.user.is_superuser
        return request.method in permissions.SAFE_METHODS or is_admin


class IsAdminOrEnrolled(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        super_user = user and user.is_superuser

        if not user.is_authenticated:
            return False

        exam_id = view.kwargs.get('examId', 0)
        enrolled = Enrollment.objects.filter(
            exam__id=exam_id, owner=user).exists()

        return super_user or enrolled


class ExamsListView(ListAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class ExamCreateView(CreateAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class ExamDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class SubjectsView(ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    #permission_classes = (IsAdminOrEnrolled, )

class SubjectsListView(ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        examId = self.kwargs['examId']
        return Subject.objects.filter(exam=examId)
    #permission_classes = (IsAdminOrEnrolled, )


class SubjectCreateView(CreateAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        examId = self.kwargs['examId']
        return Subject.objects.filter(exam=examId)
    permission_classes = (IsAdminOrReadOnly, )


class SubjectDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        examId = self.kwargs['examId']
        return Subject.objects.filter(exam=examId)
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class QuestionsPerExam(APIView):

    def get(self, request, *args, **kwargs):
        temp=[]
        examId = kwargs.get('examId', '')
        subjects = Subject.objects.filter(exam=examId)
        for subject in subjects:
            questions = Question.objects.filter(subject=subject.id)
            serializer = QuestionSerializer(questions, many=True)
            temp.append(serializer.data[0])
        return Response(temp)


class QuestionsListView(ListAPIView):
    serializer_class = QuestionSerializer
    #permission_classes = (IsAdminOrEnrolled,)

    def get_queryset(self):
        subjectId = self.kwargs['subjectId']
        return Question.objects.filter(subject=subjectId)


class QuestionCreateView(CreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        subjectId = self.kwargs['subjectId']
        return Question.objects.filter(subject=subjectId)


class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        subjectId = self.kwargs['subjectId']
        return Question.objects.filter(subject=subjectId)
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class EnrollMentView(GenericAPIView):
    def post(self, request, id=None):
        # check if user present in the request
        user = request.user
        if not user.is_authenticated:
            return Response("You are not logged in", status=status.HTTP_401_UNAUTHORIZED)

        if not id:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)

        # check if exam id exists by looing into Enrollment table
        try:
            exam = Exam.objects.get(pk=id)
        except ObjectDoesNotExist as identifier:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

        obj = Enrollment(owner=user, exam=exam)

        try:
            obj.save()
        except IntegrityError as identifier:
            return Response("You are already enrolled for this exam", status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)


class StartedView(GenericAPIView):
    permission_classes = (IsAdminOrEnrolled,)

    def post(self, request, id=None):
        # check if user present in the request
        user = request.user

        # check if exam id exists by looing into Started table
        try:
            exam = Exam.objects.get(pk=id)
        except ObjectDoesNotExist as identifier:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

        obj = Started(exam=exam, owner=user)

        try:
            obj.save()
        except:
            return Response("You already started this exam", status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)


class AnsweredView(GenericAPIView):
    permission_classes = (IsAdminOrEnrolled,)

    def post(self, request, examId=None, qid=None, option=None):
        user = request.user
        # check if question id exists by looing into Answered table
        try:
            question = Question.objects.get(pk=qid)
        except ObjectDoesNotExist as identifier:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

        obj = Answered(question=question, user=user, answer=option)

        try:
            obj.save()
        except IntegrityError as identifier:
            return Response("You already answered this question", status=status.HTTP_200_OK)

        serializers = AnsweredWithCorrectAnswerSerializer(obj)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


class AnsweredListVew(ListCreateAPIView):
    permission_classes = (IsAdminOrEnrolled,)
    serializer_class = AnsweredSerializer

    def post(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)

        serializer = self.get_serializer(
            data=request.data, many=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user = request.user
        query_set = Answered.objects.filter(user=user)
        serializer = AnsweredSerializer(query_set, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EndedExamView(GenericAPIView):
    permission_classes = (IsAdminOrEnrolled,)

    def post(self, request, id=None):
        user = request.user

        try:
            exam = Exam.objects.get(pk=id)
            obj = Started.objects.get(owner=user, exam=exam)
            obj.ended_at = datetime.now()
            obj.exam_finished = True
            obj.save()
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

        serializer = StartedSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
