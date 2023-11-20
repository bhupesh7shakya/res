from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns=[
    path('login/',UserLogin.as_view())
]