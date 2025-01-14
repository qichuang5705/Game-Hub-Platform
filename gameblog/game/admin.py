from django.contrib import admin
from django.utils.html import mark_safe
from .models import *
from django.contrib import messages
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','genre', 'datecreate', 'reward']
    search_fields = ['name', 'genre']
    list_filter = ['name', 'reward']
    readonly_fields = ['pic']

    def pic(self, Game):
        return mark_safe("<img src='/static/{img_url}' width='120px'/>".format(img_url=Game.image.name))






admin.site.register(Game, GameAdmin)
admin.site.register(Comment)