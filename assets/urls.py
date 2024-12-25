from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_asset, name='upload_asset'),
    # Các đường dẫn khác...
]