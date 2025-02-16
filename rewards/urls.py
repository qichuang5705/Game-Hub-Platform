from django.urls import path, include
from .views import TestKhungChat
urlpatterns = [
    path('test/', TestKhungChat, name="test"),
] 