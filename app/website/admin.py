from django.contrib import admin
from website.models import EventCategory, EventTag, Event, EventDateAndTime


class EventDateAndTimeInline(admin.TabularInline):
    model = EventDateAndTime


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventDateAndTimeInline]


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")
    ordering = ("name",)


@admin.register(EventTag)
class EventTagsAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")
    ordering = ("name",)
