from django.urls import path, include
from .views import DeleteComment, UpGame, GameViewset, game_detail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('game', GameViewset)

# app_name = 'gameapp' 

urlpatterns = [
    path("/game_detail/<int:id>",game_detail, name="game_detail"),
    path("/upgame",UpGame , name="upgame"),
    path("/DeleteComment/<int:comment_id>",DeleteComment , name="DeleteComment"),
    path("/API/", include(router.urls)),
]   