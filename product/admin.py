from django.contrib import admin
from .models import Product


# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
admin.site.register(Product, ProductAdmin)
