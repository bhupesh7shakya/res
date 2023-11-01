from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Category(models.Model):
    name=models.CharField(max_length=255)

class Food(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

class Table(models.Model):
    number=models.IntegerField()
    is_occupied=models.BooleanField(default=False)
    

class Order(models.Model):
    PENDING_CHOICES='P'
    ACCEPTED_CHOICES='A'
    CANCELLED_CHOICES='C'
    DELIVERD_CHOICES='D'
    STATUS_CHOICES=[
        (PENDING_CHOICES, 'Pending'),
        (ACCEPTED_CHOICES, 'Accepted'),
        (CANCELLED_CHOICES, 'Cancelled'),
        (DELIVERD_CHOICES,'Delivered')
    ]
    
    
    PAYMENT_STATUS_PEDNING_CHOICE='P'
    PAYMENT_STATUS_COMPLETED_CHOICE='P'
    
    PAYMENT_STATUS_CHOICES=[
        (PAYMENT_STATUS_COMPLETED_CHOICE,'Completed'),
        (PAYMENT_STATUS_PEDNING_CHOICE,'Pending')
    ]
    

    user=models.ForeignKey(User,on_delete=models.PROTECT)
    status=models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=PENDING_CHOICES
    )
    payment_status=models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PEDNING_CHOICE
    )


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    status=models.BooleanField(default=False)