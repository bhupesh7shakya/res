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
        
class FoodSerializer(serializers.ModelSerializer):
    
    category=serializers.StringRelatedField()
    category_id=serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category"
    )
    taxed_price=serializers.SerializerMethodField()
    class Meta:
        model=Food
        fields=[
            "id",
            "name",
            "price",
            "taxed_price",
            "category",
            "category_id",
        ]
    
    def get_taxed_price(self,food:Food):
        return food.price+(food.price*0.13)