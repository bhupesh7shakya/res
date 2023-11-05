from rest_framework import serializers
from .models import *
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=("id","name")
    


# serializer.py

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields=['id','number','is_occupied']
        
    def create(self,validated_data):
        return Table.objects.create(

            number=validated_data.get('number'),
            is_occupied=validated_data.get('is_occupied')
            
        )
    def update(self,instance:Table,validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.is_occupied = validated_data.get('is_occupied', instance.is_occupied)
        instance.save()
        return instance