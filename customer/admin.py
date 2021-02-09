from django.contrib import admin
from .models import Customer


# admin.site.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_doc', 'phone')
admin.site.register(Customer, CustomerAdmin)
