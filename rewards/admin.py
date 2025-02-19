from django.contrib import admin
from .models import FrameAvatar, FrameChat, Chat, Avatar, Inventory





@admin.register(FrameChat)
class FrameChatAdmin(admin.ModelAdmin):
  list_display = ("CssClass",'price', 'image')


@admin.register(FrameAvatar)
class FrameAvaAdmin(admin.ModelAdmin):
  list_display = ("CssClass",'price','image')

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
  list_display = ("user",'frame_chat')


@admin.register(Avatar)
class AvaAdmin(admin.ModelAdmin):
  list_display = ("user",'frame_avatar')


@admin.register(Inventory)
class InventAdmin(admin.ModelAdmin):
  list_display = ("user",'avatar', 'chat')

# @admin.register(Inventory)
# class FrameChatAdmin(admin.ModelAdmin):
#   list_display = ("user",'chat','ava')
