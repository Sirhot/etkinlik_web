from django.contrib import admin
from .models import Event, Participant

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name","date","category")
    list_display_links = ("name",)
    search_fields = ("name","category")

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'joined_at')
    list_filter = ('event',)
    search_fields = ('user__username', 'event__title')