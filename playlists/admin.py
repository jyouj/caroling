from django.contrib import admin
from adminsortable.admin import SortableAdmin
from .models import Title, Song

# Register your models here.
class TitleAdmin(SortableAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class SongAdmin(SortableAdmin):
    list_display = ('id', 'song_name', 'title')
    list_display_links = ('id', 'song_name')


admin.site.register(Title, TitleAdmin)
admin.site.register(Song, SongAdmin)
