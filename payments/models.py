from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Wallet(models.Model):
    # Mỗi user có một ví    
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE) 
    balance=models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Nạp tiền vào víví
    def recharge(self, amount):
        self.balance+=amount
        self.save()

    # Rút tiềntiền
    def withdrawals(self, amount):
        if self.balance >= amount:
            self.balance-=amount
            self.save()
            return True
        return False
    
    def __str__(self):
        return f"Ví của {self.user.username} - Số dư: {self.balance}"