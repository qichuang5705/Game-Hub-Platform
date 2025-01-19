from django.urls import path
from api import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login_page, name='login_page'),
]
