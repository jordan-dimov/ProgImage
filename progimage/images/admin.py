from django.contrib import admin

from images.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ("uuid", "height", "width")
    list_display_links = ("uuid",)


admin.site.register(Image, ImageAdmin)
