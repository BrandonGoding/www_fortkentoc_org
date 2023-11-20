from wagtail import hooks
from wagtail.admin.site_summary import PagesSummaryItem
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from website.models import BoardMember, Coach, Testimonial, EventPage


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


class EventModelAdmin(ModelAdmin):
    model = EventPage
    menu_label = "Events"
    menu_icon = "date"
    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = False
    menu_order = 3
    list_display = ('title', 'date', 'start_time', 'end_time', 'location')
    list_filter = ('title', 'date',)
    search_fields = ('title', 'date')


class TestimonialViewSet(SnippetViewSet):
    model = Testimonial
    icon = "openquote"
    inspect_view_enabled = True
    add_to_admin_menu = True
    menu_order = 100


register_snippet(BoardMemberViewSet)
register_snippet(CoachViewSet)
register_snippet(TestimonialViewSet)
modeladmin_register(EventModelAdmin)
