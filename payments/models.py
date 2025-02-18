from django.db import models, transaction
from accounts.models import CustomUser
from .paypal_config import paypalrestsdk 
from decimal import Decimal

class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="wallet")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def create_paypal_payment(self, amount, return_url, cancel_url):
        """ Tạo một yêu cầu thanh toán PayPal """
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "redirect_urls": {
                "return_url": return_url,  # URL thành công
                "cancel_url": cancel_url   # URL hủy
            },
            "transactions": [{
                "amount": {"total": str(amount), "currency": "USD"},
                "description": f"Nạp {amount} USD vào ví"
            }]
        })

        if payment.create():
            # Lấy link thanh toán PayPal
            for link in payment.links:
                if link.rel == "approval_url":
                    return link.href
        return None

    def process_paypal_payment(self, payment_id, payer_id):
        """ Xác nhận và hoàn tất thanh toán PayPal """
        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({"payer_id": payer_id}):
            amount = Decimal(payment.transactions[0].amount.total)  # Chuyển đổi thành Decimal
            with transaction.atomic():
                self.balance += amount
                self.save()
                TransactionHistory.objects.create(
                    user=self.user, transaction_type="deposit",
                    amount=amount, status="success"
                )
            return True
        return False
    def __str__(self):
        return f"Ví của {self.user.username} - Số dư: {self.balance:.2f} USD"

class TransactionHistory(models.Model):
    TRANSACTION_TYPES = [
        ("deposit", "Nạp tiền"),
        ("withdraw", "Rút tiền"),
        ("purchase", "Mua hàng"),
    ]
    STATUS_CHOICES = [
        ("success", "Thành công"),
        ("failed", "Thất bại"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    balance_after_transaction = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Thêm trường theo dõi số dư

    @classmethod
    def get_transactions_by_status(cls, user, status):
        return cls.objects.filter(user=user, status=status).order_by("-timestamp")

    @classmethod
    def get_transactions_by_type(cls, user, transaction_type):
        return cls.objects.filter(user=user, transaction_type=transaction_type).order_by("-timestamp")
    
    def __str__(self):
        return f"{self.user.username} - {self.get_transaction_type_display()} - {self.amount} USD - {self.get_status_display()} - {self.timestamp.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        verbose_name = "Lịch sử giao dịch"
        verbose_name_plural = "Lịch sử giao dịch"
        ordering = ["-timestamp"]
