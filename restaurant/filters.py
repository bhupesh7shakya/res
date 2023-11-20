from django_filters import rest_framework as filter
from .models import *
class FoodFilter(filter.FilterSet):
    class Meta:
        model=Food
        fields={
            'name':['icontains'],
            'price':['gte','lte'],
            'category':['exact',]
        }