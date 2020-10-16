from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

class CustomCreateView(GenericAPIView):


    myClass= None
    def post(self, request, **kwargs):
        
        # check if user present in the request
        user = request.user
        # if not user.is_authenticated:
        #     return Response("You are not logged in", status=status.HTTP_401_UNAUTHORIZED)

        mydictionary={}
        for field in request.data:
                if(field=='user' or '_at' in field):
                    continue
                mydictionary[field]=request.data[field]
        if(not user.is_superuser):
                mydictionary['user']=user
        else:
            if('user' in request.data):
                if(User.objects.filter(id=request.data['user']).exists()):
                    mydictionary['user']=User.objects.get(id=request.data['user'])
                else:
                    return Response("User does not exist", status=status.HTTP_400_BAD_REQUEST)
        
        obj = self.myClass(**mydictionary)

        for field in obj.__dict__:
            if(field=='id' or field=='user_id'):
                continue
            if(not type(obj.__dict__[field]) == bool or '_at' in field):
                if (not obj.__dict__[field]):
                    return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)


        try:
            obj.save()
        except IntegrityError as identifier:
            return Response("Data already Exists", status=status.HTTP_200_OK)

        return Response("Created", status=status.HTTP_200_OK)


class CustomUpdateView(GenericAPIView):

    myClass=None

    def put(self, request ,id=None):
        
        # check if user present in the request
        user = request.user
        if not user.is_authenticated:
            return Response("You are not logged in", status=status.HTTP_401_UNAUTHORIZED)

        if not id:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)


        try:
            obj = self.myClass.objects.get(pk=id)
        except ObjectDoesNotExist as identifier:
            return Response("User Not found", status=status.HTTP_404_NOT_FOUND)

        #loops though request.data and address object and sets them accordingly
        #skips loop if field is equal to user or datefield or empty
        for field in request.data:
                if(field=='user' or '_at' in field or not request.data[field]):
                    continue
                obj.__dict__[field]=request.data[field]

        #if user is not admin, sets address's foreign key 'user' to current logged in user
        if(not user.is_superuser):           
            obj.user=user
        else:
            #else sets it to id input by admin
            if 'user' in request.data.keys(): 
                obj.user=User.objects.get(id=request.data['user'])
        

        try:
            obj.save()
        except IntegrityError as identifier:
            return Response("Data already Exists", status=status.HTTP_200_OK)

        return Response("Fields updated",status=status.HTTP_200_OK)