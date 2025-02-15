from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from .models import Wallet

# Khi user được tạo kích hoạt hàm nàynày
@receiver(post_save, sender=CustomUser)
def create_wallet(sender, instance, created, **kwargs):
    # Kiểm tra nếu user mới được tạo 
    if created:
        Wallet.objects.create(user=instance)