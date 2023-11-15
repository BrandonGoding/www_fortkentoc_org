from wagtail import hooks
from wagtail.admin.site_summary import PagesSummaryItem
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from website.models import BoardMember, Coach, Event, Testimonial


@hooks.register('construct_main_menu')
def hide_page_explorer_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'explorer']


@hooks.register('construct_homepage_summary_items', order=1)
def remove_pages_summary_item(request, summary_items):
    summary_items[:] = [i for i in summary_items if not isinstance(i, PagesSummaryItem)]


class BoardMemberViewSet(SnippetViewSet):
    model = BoardMember
    icon = "group"
    inspect_view_enabled = True
    add_to_admin_menu = True
    menu_order = 1


class CoachViewSet(SnippetViewSet):
    model = Coach
    icon = "user"
    inspect_view_enabled = True
    add_to_admin_menu = True
    menu_order = 2


class EventViewSet(SnippetViewSet):
    model = Event
    icon = "date"
    inspect_view_enabled = True
    add_to_admin_menu = True
    menu_order = 3


class TestimonialViewSet(SnippetViewSet):
    model = Testimonial
    icon = "openquote"
    inspect_view_enabled = True
    add_to_admin_menu = True
    menu_order = 100


register_snippet(BoardMemberViewSet)
register_snippet(CoachViewSet)
register_snippet(EventViewSet)
register_snippet(TestimonialViewSet)
