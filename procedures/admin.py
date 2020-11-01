from django.contrib import admin
from .models import Procedure

admin.site.register(Procedure)

class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'body')
