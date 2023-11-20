from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.validators import ValidationError
from .serializers import *
# Create your views here.

class UserLogin(APIView):
    def post(self,request):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        user=authenticate(
            username=serializer.validated_data.get('username')
            ,password=serializer.validated_data.get('password')
        )
        
        if user:
            token,_=Token.objects.get_or_create(user=user)
            return Response({
                'token':token.key,
            })
        else:
            return Response({
                'details':'Invalid credentials'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
            
# create api of user