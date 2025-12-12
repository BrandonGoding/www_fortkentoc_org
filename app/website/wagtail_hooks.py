from .models import Map, BoardMember, Coach, Event
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from wagtail import hooks


class BoardMemberAdmin(ModelAdmin):
    model = BoardMember
    menu_label = "Board Members"
    menu_icon = "user"
    menu_order = 198
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "role")
    search_fields = "name"


class CoachAdmin(ModelAdmin):
    model = Coach
    menu_label = "Coaches"
    menu_icon = "group"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "title")
    search_fields = "name"


class EventAdmin(ModelAdmin):
    model = Event
    menu_label = "Events"
    menu_icon = "site"
    menu_order = 203
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)
    search_fields = ("name",)


class MapAdmin(ModelAdmin):
    model = Map
    menu_label = "Maps"
    menu_icon = "site"
    menu_order = 204
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "category")
    search_fields = ("title",)


modeladmin_register(BoardMemberAdmin)
modeladmin_register(CoachAdmin)
modeladmin_register(MapAdmin)
modeladmin_register(EventAdmin)


# Hide "Pages" (the Explorer) from the main sidebar
@hooks.register("construct_main_menu")
def hide_pages_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "explorer"]


# Hide "Sites" from Settings
@hooks.register("construct_settings_menu")
def hide_sites_settings_item(request, menu_items):
    menu_items[:] = [
        item for item in menu_items if getattr(item, "name", "") != "sites"
    ]
