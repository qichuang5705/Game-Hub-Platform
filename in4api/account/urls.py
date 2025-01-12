from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/",signup , name="signup"),
    
    #path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login/",auth_views.LoginView.as_view(template_name='login.html') , name="login"),
    path("accounts/logout/",auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path("", home, name="home"),
    path("in4user/",in4 , name="in4user"),
]