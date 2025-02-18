from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Frame(models.Model):
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to="rewards/", default="default/gojo.jpg")
    class Meta:
        abstract = True

    def __str__(self):
        return self.CssClass
    
class FrameChat(Frame):
    CssClass = models.TextField(max_length=50, default="default-chat")
    
class FrameAvatar(Frame):
    CssClass = models.TextField(max_length=50, default="default-avatar")

class Chat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="chat_class")
    frame_chat = models.ForeignKey(FrameChat, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.frame_chat.CssClass

class Avatar(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="avatar_class")
    frame_avatar = models.ForeignKey(FrameAvatar, on_delete=models.CASCADE)


    def __str__(self):
        return self.frame_avatar.CssClass


class Inventory(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="invent")
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

<<<<<<< HEAD
 




<<<<<<< HEAD
=======

# @receiver(post_save, sender=CustomUser)
# def create_inventory_for_user(sender, instance, created, **kwargs):
#     if created:
#         inventory = Inventory.objects.create(user=instance)
#         default_chat, _ = FrameChat.objects.get_or_create(CssClass="default-chat")
#         default_ava, _ = FrameAva.objects.get_or_create(CssClass="default-ava")
#         inventory.chat_frames.add(default_chat)  # Sử dụng .add() để thêm khung chat vào inventory
#         inventory.ava_frames.add(default_ava)  # Sử dụng .add() để thêm khung avatar vào inventory
>>>>>>> lab
=======
@receiver(post_save, sender=CustomUser)
def create_default_frames(sender, instance, created, **kwargs):
    if created:
        print("Tạo mặc định")
        frame_chat, _ = FrameChat.objects.get_or_create(CssClass="default-chat")
        frame_avatar, _ = FrameAvatar.objects.get_or_create(CssClass="default-avatar")
        chat = Chat.objects.create(user=instance, frame_chat=frame_chat)
        avatar = Avatar.objects.create(user=instance, frame_avatar=frame_avatar)
        Inventory.objects.create(user=instance,chat=chat, avatar=avatar)
>>>>>>> lab
