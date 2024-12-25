from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.game_list, name='game_list'),
    path('leaderboard/<int:game_id>/', views.game_leaderboard, name='game_leaderboard'),
    path('review/<int:game_id>/', views.submit_review, name='submit_review'),
    # Các đường dẫn khác...
]