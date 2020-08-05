from django.urls import path, include 
from rest_framework import routers
from .views import ItemViewSet

# create a variable 
router = routers.DefaultRouter()
router.register('item',ItemViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
