from django.contrib import admin
from .models import TableRewards, FrameChat

@admin.register(TableRewards)
class TableRewardsAdmin(admin.ModelAdmin):
    list_display = ("userid", "framechat")  # Hiển thị các cột trong danh sách



@admin.register(FrameChat)
class FrameChatAdmin(admin.ModelAdmin):
    list_display = ("CssClass", "code")  # Hiển thị các cột trong danh sách