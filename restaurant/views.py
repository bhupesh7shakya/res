from django.shortcuts import render
from .models import *
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer=CategorySerializer(categories,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)