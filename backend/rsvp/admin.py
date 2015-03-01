"""
RSVP Module Admin Site Config
"""
from django.contrib import admin

from rsvp.models import Guest, Invite


class GuestInline(admin.TabularInline):
    extra = 0
    fields = ['name', ]
    min_num = 1
    model = Guest


@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    fields = ['description', 'code', ]
    inlines = [GuestInline, ]
    list_display = ('description', 'code', )
