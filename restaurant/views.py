from django.shortcuts import render,get_object_or_404
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status,generics,viewsets

from rest_framework.decorators import api_view ,APIView



class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer

# views.py


class TableViewSet(viewsets.ModelViewSet):
    queryset=Table.objects.all()
    serializer_class=TableSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset=Food.objects.select_related('category').all()
    serializer_class=FoodSerializer