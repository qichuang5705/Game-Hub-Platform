from django.contrib import admin
from django.urls import include, path
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('UploadAssset' , views.AssetViewSet)
urlpatterns = [
    path('',include(router.urls)),
]