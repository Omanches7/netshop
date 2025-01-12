from django.contrib import admin
from .models import products, offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(offer,)
admin.site.register(products, ProductAdmin)
