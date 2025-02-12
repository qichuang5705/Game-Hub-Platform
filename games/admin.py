from django.contrib import admin

# Register your models here.

from .models import Game, Genre, LBHistory

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'datecreate', 'reward')
    filter_horizontal = ('genres',)  # Hiển thị danh sách thể loại để chọn

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(LBHistory)
class LBAdmin(admin.ModelAdmin):
    list_display = ('games', 'users', 'score', 'date')

