from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from .CustomViews import *

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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class ExamCreateView(CreateAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class ExamDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class SubjectsListView(ListAPIView):
    serializer_class = SubjectSerializer
    def get_queryset(self):
        examId = self.kwargs['examId']
        return Subject.objects.filter(exam=examId)
    permission_classes = (IsAdminOrEnrolled, )

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


class QuestionsListView(ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminOrEnrolled,)

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

# class StartedView(CreateAPIView):
#     serializer_class = StartedSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     def perform_create(self, serializer, id=None):
#         print(self.kwargs)
#         id = self.kwargs.get('id', None)

#         try:
#             exam = Exam.objects.get(pk=id)
#             serializer.save(owner=self.request.user, exam=exam)
#         except ObjectDoesNotExist as identifier:
#             return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)


class StartedView(GenericAPIView):
    def post(self, request, id=None):
        # check if user present in the request
        user = request.user
        if not user.is_authenticated:
            return Response("You are not logged in", status=status.HTTP_401_UNAUTHORIZED)

        if not id:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)

        # check if exam id exists by looing into Started table
        try:
            exam = Exam.objects.get(pk=id)
        except ObjectDoesNotExist as identifier:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

        obj = Started(owner=user, exam=exam)

        try:
            obj.save()
        except IntegrityError as identifier:
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

class AddressCreateView(CustomCreateView):
    serializer_class=AddressSerializer
    myClass=Address

class AddressUpdateView(CustomUpdateView):
    serializer_class=AddressSerializer
    myClass=Address  

class AddressRetrieveView(RetrieveAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    lookup_field = "id"


class AddressDeleteView(DestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class ConfigurationCreateView(CustomCreateView):
    serializer_class=ConfigurationSerializer
    myClass=Configuration

class ConfigurationUpdateView(CustomUpdateView):
    serializer_class=ConfigurationSerializer
    myClass=Configuration 

class ConfigurationRetrieveView(RetrieveAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()
    lookup_field = "id"


class ConfigurationDeleteView(DestroyAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class ContactCreateView(CustomCreateView):
    serializer_class=ContactSerializer
    myClass=Contact

class ContactUpdateView(CustomUpdateView):
    serializer_class=ContactSerializer
    myClass=Contact 

class ContactRetrieveView(RetrieveAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = "id"


class ContactDeleteView(DestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

class FeedbackCreateView(CustomCreateView):
    serializer_class=FeedbackSerializer
    myClass=Feedback

class FeedbackUpdateView(CustomUpdateView):
    serializer_class=FeedbackSerializer
    myClass=Feedback 

class FeedbackRetrieveView(RetrieveAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    lookup_field = "id"


class FeedbackDeleteView(DestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )

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


class CitiesListView(ListCreateAPIView):
    serializer_class = CitiesSerializer
    queryset = Cities.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class CitiesDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CitiesSerializer
    queryset = Cities.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )
   
class BloodgroupListView(ListCreateAPIView):
    serializer_class = BloodgroupSerializer
    queryset = Bloodgroup.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class BloodgroupDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BloodgroupSerializer
    queryset = Bloodgroup.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class CountriesListView(ListCreateAPIView):
    serializer_class = CountriesSerializer
    queryset = Countries.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class CountriesDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CountriesSerializer
    queryset = Countries.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )


class CurrenciesListView(ListCreateAPIView):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class CurrenciesDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()
    lookup_field = "id"
    permission_classes = (IsAdminOrReadOnly, )
