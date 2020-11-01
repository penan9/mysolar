from django.contrib import admin
from .models import About


admin.site.register(About)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'sequence', 'body')
