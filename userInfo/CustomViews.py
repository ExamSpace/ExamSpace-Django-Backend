from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

class CustomCreateUpdateView(GenericAPIView):


    myClass= None
    def post(self, request, **kwargs):
        
        # check if user present in the request
        user = request.user
        if not user.is_authenticated:
            return Response("You are not logged in", status=status.HTTP_401_UNAUTHORIZED)

        mydictionary={}
        mydictionary['user']=user
        for field in request.data:
                if(field=='user' or '_at' in field):
                    continue
                mydictionary[field]=request.data[field]     

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

    def put(self, request, **kwargs):
        
        # check if user present in the request
        user = request.user
        if not user.is_authenticated:
            return Response("You are not logged in", status=status.HTTP_401_UNAUTHORIZED)


        try:
            obj = self.myClass.objects.get(user=user)
        except ObjectDoesNotExist as identifier:
            return Response("Data For User Not found", status=status.HTTP_404_NOT_FOUND)

        #loops though request.data and address object and sets them accordingly
        #skips loop if field is equal to user or datefield or empty
        for field in request.data:
                if(field=='user' or '_at' in field or not request.data[field]):
                    continue
                obj.__dict__[field]=request.data[field]

        obj.user = user        

        try:
            obj.save()
        except IntegrityError as identifier:
            return Response("Data already Exists", status=status.HTTP_200_OK)

        return Response("Fields updated",status=status.HTTP_200_OK)