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
    


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=[
            "food",
        ]



class SimpleOrderSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model=Order
        fields=[
            'id',
            'status',
            'payment_status',
        ]
    
    def update(self, instance:Order, validated_data):
        instance.status=Order.DELIVERD_CHOICES
        instance.PAYMENT_STATUS_COMPLETED_CHOICE
        instance.save()
        return instance
        

class OrderSerializer(serializers.ModelSerializer):
    # user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    items=OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=[
            'id',
            'user',
            'table',
            'status',
            'payment_status',
            "items",
        ]
        
    def create(self, validated_data):
        items=validated_data.get('items')
        order=Order.objects.create(
            user=validated_data.get('user'),
            table=validated_data.get('table')
        )
        # raise Exception(items[0]['food'])
        order_item_objects=[
            OrderItem(
                food=item.get('food'),
                order=order
            )
            for item in items
        ]
        
        OrderItem.objects.bulk_create(order_item_objects)
        
        return order
        