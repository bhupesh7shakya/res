from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ADMIN_ROLE='A'
    WAITER_ROLE='W'
    
    ROLE_CHOICES=[
        (ADMIN_ROLE,'ADMIN'),
        (WAITER_ROLE,'WAITER')
    ]
    
    phone_number=models.CharField(max_length=10,null=True)
    role=models.CharField(max_length=1,choices=ROLE_CHOICES,null=True)