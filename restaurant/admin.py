from django.contrib import admin
from .models import *

from django import forms

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_per_page=10
    search_fields=('name',)



@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "price",
        "category",
    )
    list_filter=('category',)
    search_fields=('name','price',)
    list_per_page=10
    autocomplete_fields=('category',)
    



@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    # list_display=()
    pass


class OrderItemInLine(admin.StackedInline):
    
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=(
        "user",
        "status",
        "payment_status",
    )
    # autocomplete_fields=('',)
    inlines=(OrderItemInLine,)
    
    



# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     # list_display=()
#     pass

