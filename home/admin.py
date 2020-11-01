from django.contrib import admin
from .models import Home, Image


class ImageAdmin(admin.ModelAdmin):
#    pass
    list_display = ('name', 'directory', 'file')


class HomeAdmin(admin.ModelAdmin):
#    pass
    list_display = ('name', 'file')


# Register your models here.
admin.site.register(Home, HomeAdmin)
admin.site.register(Image, ImageAdmin)
