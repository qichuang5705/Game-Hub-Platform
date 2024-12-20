from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('loginas', views.login, name="login"),
    path('loginas/register', views.register, name="register"),
]
