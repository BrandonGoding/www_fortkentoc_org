from .models import Map, BoardMember, Coach, DayPassLink, Event
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

class BoardMemberAdmin(ModelAdmin):
    model = BoardMember
    menu_label = "Board Members"
    menu_icon = "user"
    menu_order = 198
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "role")
    search_fields = ("name")
    
class CoachAdmin(ModelAdmin):
    model = Coach
    menu_label = "Coaches"
    menu_icon = "group"
    menu_order = 199
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "title")
    search_fields = ("name")

class EventAdmin(ModelAdmin):
    model = Event
    menu_label = "Events"
    menu_icon = "site"  # Choose an icon from https://docs.wagtail.org/en/stable/reference/icons.html
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)
    search_fields = ("name",)

class PasslinkAdmin(ModelAdmin):
    model = DayPassLink
    menu_label = "Day Passes"
    menu_icon = "tag"
    menu_order = 199
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "price")
    search_fields = ("name")

class MapAdmin(ModelAdmin):
    model = Map
    menu_label = "Maps"
    menu_icon = "site"  # Choose an icon from https://docs.wagtail.org/en/stable/reference/icons.html
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "category")
    search_fields = ("title",)
    
modeladmin_register(BoardMemberAdmin)
modeladmin_register(CoachAdmin)
modeladmin_register(MapAdmin)
modeladmin_register(PasslinkAdmin)
modeladmin_register(EventAdmin)