from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('upgrade/', views.upgrade_role, name="upgrade"),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path("accounts/information/", views.information , name="information"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
]
