from django.urls import path
from . import views

urlpatterns = [
    path('logs/', views.admin_logs, name='admin_logs'),
    # Các đường dẫn khác...
]