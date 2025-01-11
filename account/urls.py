from django.urls import path, include
from .views import *

urlpatterns = [
    path("signup/",signup , name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home, name="home"),
]