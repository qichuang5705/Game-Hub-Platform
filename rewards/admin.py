from django.contrib import admin
from .models import FrameChat, FrameAva, Inventory




@admin.register(FrameChat)
class FrameChatAdmin(admin.ModelAdmin):
  list_display = ("CssClass",'price')  # Hiển thị các cột trong danh sách

@admin.register(FrameAva)
class FrameAvaAdmin(admin.ModelAdmin):
    list_display = ("CssClass",'price')  # Hiển thị các cột trong danh sách


# @admin.register(Shop)
# class FrameChatAdmin(admin.ModelAdmin):
#   list_display = ("chat_frames",'ava_frames')

# @admin.register(Inventory)
# class FrameChatAdmin(admin.ModelAdmin):
#   list_display = ("user",'chat','ava')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('user',)