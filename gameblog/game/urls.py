from django.urls import path, include
from .views import *


urlpatterns = [
    path("game/<int:id>",game , name="game"),
    path("DeleteComment/<int:comment_id>",DeleteComment , name="DeleteComment"),
]