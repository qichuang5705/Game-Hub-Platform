from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Inventory(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Một người dùng có một Inventory



class Frame(models.Model):
    CssClass = models.CharField(max_length=100, blank=True)
    price = models.IntegerField(default=100)
    def __str__(self):
        return self.CssClass
    
    class Meta:
        abstract = True  

class FrameAva(Frame):
    CssClass = models.CharField(max_length=100, default="default-ava")
    


class FrameChat(Frame):
    CssClass = models.CharField(max_length=100, default="default-chat")

class FrameChatSohuu(Frame):
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE)


class FrameAvaSohuu(Frame):
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE)



 





# @receiver(post_save, sender=CustomUser)
# def create_inventory_for_user(sender, instance, created, **kwargs):
#     if created:
#         inventory = Inventory.objects.create(user=instance)
#         default_chat, _ = FrameChat.objects.get_or_create(CssClass="default-chat")
#         default_ava, _ = FrameAva.objects.get_or_create(CssClass="default-ava")
#         inventory.chat_frames.add(default_chat)  # Sử dụng .add() để thêm khung chat vào inventory
#         inventory.ava_frames.add(default_ava)  # Sử dụng .add() để thêm khung avatar vào inventory
