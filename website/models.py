from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index
from wagtail import blocks
from website.blocks import ImagesWithHeadingAndDescription, BoardMemberBlock


class EventLocationChoices(models.TextChoices):
    FKOC_ARENA = 'fkoc_arena', 'FKOC Arena'
    FKOC_LODGE = 'fkoc_lodge', 'FKOC Lodge'
    FKOC_WAX_BUILDING = 'fkoc_wax_building', 'FKOC Wax Building'


class HomePage(Page):
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["event_listings"] = EventPage.objects.live().order_by("event_date")
        return context


class WhoWeArePage(Page):
    max_count = 1

    body = StreamField([
        ('board_members', blocks.ListBlock(BoardMemberBlock()))
    ], use_json_field=True, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class FacilitiesPage(Page):
    max_count = 1


class PoliciesPage(Page):
    max_count = 1


class EventListingPage(Page):
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["events"] = EventPage.objects.live().order_by("event_date")
        return context


class EventPage(Page):
    banner_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    event_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=17, choices=EventLocationChoices.choices, default=EventLocationChoices.FKOC_LODGE)
    body = StreamField([
        ('images_with_heading_and_description', ImagesWithHeadingAndDescription()),
    ], use_json_field=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('event_date'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('event_date'),
        FieldPanel('start_time'),
        FieldPanel('end_time'),
        FieldPanel('location'),
        FieldPanel('banner_image'),
    ]

    parent_page_types = ['website.EventListingPage']

    def __str__(self):
        return f"{self.title}"
