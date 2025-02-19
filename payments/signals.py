from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from .models import Wallet

@receiver(post_save, sender=CustomUser)
def create_wallet(sender, instance, created, **kwargs):
    """Tự động tạo ví cho user mới"""
    if created:
        try:
            Wallet.objects.get_or_create(user=instance)
        except Exception as e:
            print(f"Lỗi khi tạo ví cho {instance.username}: {e}")
