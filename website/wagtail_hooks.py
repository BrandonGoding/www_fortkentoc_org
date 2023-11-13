from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from website.models import BoardMember, Coach


class BoardMemberViewSet(SnippetViewSet):
    model = BoardMember
    icon = "group"
    menu_label = "Board Members"
    menu_name = "board_members"
    menu_order = 1
    add_to_admin_menu = True


class CoachViewSet(SnippetViewSet):
    model = Coach
    icon = "user"
    menu_label = "Coaches"
    menu_name = "coaches"
    menu_order = 2
    add_to_admin_menu = True


register_snippet(BoardMemberViewSet)
register_snippet(CoachViewSet)
