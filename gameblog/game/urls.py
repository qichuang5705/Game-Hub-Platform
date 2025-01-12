from django.urls import path, include
from .views import *


urlpatterns = [
    path("game/<int:id>",game , name="game"),
]