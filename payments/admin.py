from django.contrib import admin

from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)
class GameAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')