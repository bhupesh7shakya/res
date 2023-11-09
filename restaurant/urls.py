from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('categories',CategoryViewSet,basename="category")
router.register('tables',CategoryViewSet,basename="table")
router.register('foods',FoodViewSet,basename="food")
urlpatterns = [
   
    
]+router.urls
