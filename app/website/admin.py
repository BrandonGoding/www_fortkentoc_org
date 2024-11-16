from django.contrib import admin
from website.models import Event, ProgramDate, EventTag, EventCategory


class ProgramDateInline(admin.TabularInline):
    model = ProgramDate


class EventAdmin(admin.ModelAdmin):
    inlines = [
        ProgramDateInline
    ]


admin.site.register(Event, EventAdmin)
admin.site.register(EventTag)
admin.site.register(EventCategory)
