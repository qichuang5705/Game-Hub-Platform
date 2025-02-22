from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)
class GameAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')


<<<<<<< HEAD
=======
from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)
class GameAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
>>>>>>> 0f13a843367379f007e753e7f5efc5aab238ea99
