from .models import Map, BoardMember
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

class BoardMemberAdmin(ModelAdmin):
    model = BoardMember
    menu_label = "Board Members"
    menu_icon = "user"
    menu_order = 199
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "role")
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
modeladmin_register(MapAdmin)
