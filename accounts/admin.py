from django.contrib import admin
from .models import CustomUser

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'date_joined']
    search_fields = ['username', 'email', 'role']
    list_filter = ['role', 'date_joined']

admin.site.register(CustomUser, UserAdmin)