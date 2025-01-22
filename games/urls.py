from django.urls import path, include
from .views import DeleteComment, UpGame, game_detail, Delete_Game
from rest_framework.routers import DefaultRouter

# app_name = 'gameapp' 

urlpatterns = [
    path("game_detail/<int:id>",game_detail, name="game_detail"),
    path("up_game",UpGame , name="up_game"),
    path("DeleteComment/<int:comment_id>",DeleteComment , name="DeleteComment"),
    path("Delete_Game/<int:game_id>", Delete_Game , name="Delete_Game"),
]   