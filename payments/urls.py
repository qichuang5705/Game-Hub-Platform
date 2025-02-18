from django.urls import path
from . import views

urlpatterns = [
    path("deposit/", views.deposit_page, name="deposit_page"),
    path("create-payment/", views.create_payment, name="create_payment"),
    path("execute-payment/", views.execute_payment, name="execute_payment"),
    path("payment-failed/", views.payment_failed, name="payment_failed"),
    path("history/", views.transaction_history, name="transaction_history"),
    path("withdraw_to_paypal/", views.withdraw_to_paypal, name="withdraw_to_paypal"),
]