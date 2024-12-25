from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_dashboard, name='account_dashboard'),  # Accounts dashboard or homepage
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
]