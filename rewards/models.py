from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class FrameChat(models.Model):
    CssClass = models.CharField(max_length=100, default="default-chat")
    code = models.TextField(null=True)

    def __str__(self):
        return self.CssClass

class TableRewards(models.Model):
    userid = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    framechat = models.ForeignKey(FrameChat, on_delete=models.CASCADE)

#Tự động tạo tablereward khi custumusser được tạo
@receiver(post_save, sender=CustomUser)
def create_tabel_rewards(sender, instance, created, **kwargs):
    if created:  # Chỉ tạo khi user mới được tạo
        default_framechat, _ = FrameChat.objects.get_or_create(
        
            defaults={"code": "Default code"}
        )
        TableRewards.objects.create(userid=instance, framechat=default_framechat)