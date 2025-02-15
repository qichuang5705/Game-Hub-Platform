from django.urls import path
from .views import create_payment, paypal_success, paypal_cancel

urlpatterns = [
    path("paypal/", create_payment, name="paypal_payment"),
    path("paypal-success/", paypal_success, name="paypal_success"),
    path("paypal-cancel/", paypal_cancel, name="paypal_cancel"),
]