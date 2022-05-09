from django.contrib import admin

# Register your models here.
from .models import (Profile, Links)

admin.site.register(Profile)

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('Link_Name', 'get_authors')