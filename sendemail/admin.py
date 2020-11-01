from django.contrib import admin

# Register your models here.
from .models import ContactFormModel


class ContactFormModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'message')


admin.site.register(ContactFormModel, ContactFormModelAdmin)
