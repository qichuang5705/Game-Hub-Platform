from django.contrib import admin
from .models import asset
admin.site.register(asset)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('price', 'type', 'description','quantifier','title','thumnail')  
