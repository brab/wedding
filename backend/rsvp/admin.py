"""
RSVP Module Admin Site Config
"""
from django.contrib import admin

from rsvp.models import Event, Guest, GuestGroup


class EventInline(admin.TabularInline):
    extra = 0
    min_num = 1
    model = Guest.events.through


class GuestGroupInline(admin.TabularInline):
    extra = 0
    min_num = 1
    model = GuestGroup


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'datetime_start', 'datetime_end', ]
    list_display = ('name', 'datetime_start', )


@admin.register(GuestGroup)
class GuestGroupAdmin(admin.ModelAdmin):
    fields = ['code', 'responded', ]
    list_display = ['code', 'responded', ]


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    fields = ['name', 'group', ]
    list_display = ['name', 'group', ]
    inlines = [EventInline, ]
