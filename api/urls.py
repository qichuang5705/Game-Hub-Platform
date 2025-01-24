from django.urls import path
from api import views

urlpatterns = [
    path('', views.base, name='base'),
    path('game/', views.base, name='page_game'),
]
