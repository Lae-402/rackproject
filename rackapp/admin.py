from django.contrib import admin

from .models import Media, Artist, Rack


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class RackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Media, MediaAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Rack, RackAdmin)