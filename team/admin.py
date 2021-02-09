from django.contrib import admin
from .models import Team


# admin.site.register(Team)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(Team, TeamAdmin)
