from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver



class Frame(models.Model):
    CssClass = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    is_buy = models.BooleanField(default=False)
    def __str__(self):
        return self.CssClass
    
    class Meta:
        abstract = True  

class FrameAva(Frame):
    CssClass = models.CharField(max_length=100, default="default-ava")
    

class FrameChat(Frame):
    CssClass = models.CharField(max_length=100, default="default-chat")



class Shop(models.Model):
    chat = models.ForeignKey(FrameChat, on_delete=models.CASCADE)
    ava = models.ForeignKey(FrameAva, on_delete=models.CASCADE)

 

class Inventory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chat = models.ForeignKey(FrameChat,blank=True, null=True, on_delete=models.CASCADE)
    ava = models.ForeignKey(FrameAva,blank=True, null=True, on_delete=models.CASCADE)




@receiver(post_save, sender=CustomUser)
def create_inventory_for_user(sender, instance, created, **kwargs):
    if created:
        default_chat, _ = FrameChat.objects.create(CssClass="default-chat", )

        default_ava, _ = FrameAva.objects.create(CssClass="default-ava")

        Inventory.objects.create(user=instance, chat=default_chat, ava=default_ava)