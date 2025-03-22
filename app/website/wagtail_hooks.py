from wagtail import hooks
from .models import BoardMember, Coach
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

@hooks.register('construct_main_menu')
def remove_unwanted_main_menu_items(request, menu_items):
    items_to_remove = ['explorer', 'help', 'search', 'documents', 'reports', 'images']
    menu_items[:] = [item for item in menu_items if item.name not in items_to_remove]

@hooks.register('construct_settings_menu')
def keep_only_users_in_settings_menu(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name == 'users']


class BoardMemberViewSet(SnippetViewSet):
    model = BoardMember
    icon = "user"
    copy_view_enabled = False
    inspect_view_enabled = True
    menu_label = "Board Members"
    menu_name = "board_members"
    menu_order = 300
    add_to_admin_menu = True

class CoachViewSet(SnippetViewSet):
    model = Coach
    icon = "user"
    copy_view_enabled = False
    inspect_view_enabled = True
    menu_label = "Coaches"
    menu_name = "coaches"
    menu_order = 301
    add_to_admin_menu = True

register_snippet(BoardMemberViewSet)
register_snippet(CoachViewSet)
