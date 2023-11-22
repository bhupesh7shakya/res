from django.shortcuts import render,get_object_or_404
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status,generics,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view ,APIView
from .filters import *
from .permissions import IsAuthenticatedOrReadOnly



class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)

    
    
# views.py


class TableViewSet(viewsets.ModelViewSet):
    queryset=Table.objects.all()
    serializer_class=TableSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)

class FoodViewSet(viewsets.ModelViewSet):
    queryset=Food.objects.select_related('category').all()
    serializer_class=FoodSerializer
    pagination_class=PageNumberPagination
    # filter_backends=(DjangoFilterBackend,)
    filterset_class=FoodFilter
    
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.prefetch_related('items').all()
    serializer_class=OrderSerializer
    permission_classes=(IsAuthenticated,)
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return SimpleOrderSerialzer
        return OrderSerializer
    
    
    def get_queryset(self):
        # user=self.request.user
        user=self.request.user
        return  Order.objects.prefetch_related('items').filter(user=user,status=Order.PENDING_CHOICES)