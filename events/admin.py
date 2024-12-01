from django.contrib import admin
from .models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name","date","category")
    list_display_links = ("name",)
    search_fields = ("name","category")