from django.urls import path
from . import views

urlpatterns = [
    path('payment-info/', views.payment_info, name='payment_info'),
    # Các đường dẫn khác...
]