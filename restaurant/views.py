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

class TableList(APIView):
    def get(self,request):
        queryset=Table.objects.all()
        serializer=TableSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        try:
            serializer=TableSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)



class TableDetail(APIView):

    def get(self,request,pk):
        table= get_object_or_404(Table, pk=pk)
        serializer = TableSerializer(table)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        table= get_object_or_404(Table, pk=pk)
        serializer = TableSerializer(instance=table, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Data has been updated"}, status=status.HTTP_200_OK)

    def delete(elf,request,pk):
        table= get_object_or_404(Table, pk=pk)
        table.delete()
        return Response({"detail": "Data has been deleted"}, status=status.HTTP_204_NO_CONTENT)