from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('categories',CategoryViewSet,basename="category")
urlpatterns = [
   
    
]+router.urls
