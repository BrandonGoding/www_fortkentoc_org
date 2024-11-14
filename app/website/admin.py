from django.contrib import admin
from website.models import Event, ProgramDate


class ProgramDateInline(admin.TabularInline):
    model = ProgramDate


class EventAdmin(admin.ModelAdmin):
    inlines = [
        ProgramDateInline
    ]


admin.site.register(Event, EventAdmin)
