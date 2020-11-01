from django.contrib import admin
from .models import Offer, Product, ProductDetail


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('productid', 'product', 'title', 'desc', 'directory', 'photo', 'date')
    readonly_fields=('productid', 'thumbnail')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('code2', 'doc')
    list_display = ('id', 'name', 'code', 'stock', 'price', 'price2', 'unit', 'photo', 'doc', 'youtubeID')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
