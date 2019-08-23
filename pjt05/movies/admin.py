from django.contrib import admin
from .models import Movies
# Register your models here.

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_en', 'audience', 'open_date', 'genre', 'watch_grade', 'score', 'poster_url', 'description')