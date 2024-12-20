from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login2', views.login, name="login"),
    path('login2/register', views.register, name="register"),
]
