from django.contrib import admin
from .models import Sport


# admin.site.register(Sport)

class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(Sport, SportAdmin)
