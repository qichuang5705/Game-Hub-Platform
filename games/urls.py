from django.urls import path, include
from .views import DeleteComment, UpGame, game_detail
from rest_framework.routers import DefaultRouter

# app_name = 'gameapp' 

urlpatterns = [
    path("game_detail/<int:id>",game_detail, name="game_detail"),
    path("up_game",UpGame , name="up_game"),
    path("DeleteComment/<int:comment_id>",DeleteComment , name="DeleteComment"),
]   