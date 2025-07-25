from django.core.exceptions import ValidationError
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    FieldRowPanel,
)
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from .fields import TemplateChoiceWidget
from wagtailmetadata.models import MetadataPageMixin
from datetime import date
from wagtail.snippets.models import register_snippet
import uuid
from modelcluster.models import ClusterableModel

class HomePage(MetadataPageMixin, Page):
    max_count = 1
    subpage_types = [
        "website.UpcomingListingPage",
        "website.LegacyPage",
        "website.AboutUsPage",
        "website.ProgramsPage",
        "website.ActivitiesPage",
        "website.DayPassesPage",
        "website.TrailsPage",
    ]
    main_title = models.CharField(max_length=100, blank=True, null=True)
    main_content = RichTextField(blank=True)
    main_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    cta_text = models.CharField(max_length=100, blank=True, null=True)
    cta_url = models.URLField(blank=True, null=True)
    cta_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = (
        Page.content_panels

        + [
            FieldPanel("main_title"),
            FieldPanel("main_content"),
            FieldPanel("main_image"),
            FieldPanel("cta_text"),
            FieldPanel("cta_page"),
            FieldPanel("cta_url"),
        ]
    )


class UpcomingListingPage(MetadataPageMixin, Page):
    parent_page_types = ["website.HomePage"]
    subpage_types = []
    max_count = 2

    def get_template(self, request, *args, **kwargs):
        return "website/event_listing_page.html"
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # TODO: Only show current events
        context["events"] = Event.objects.all()
        return context


#################### OLD PAGES ####################
class LegacyPage(MetadataPageMixin, Page):
    subpage_types = ["website.HomePage"]
    template_name = models.CharField(
        max_length=255, default="default_template.html"
    )

    content_panels = (
        Page.content_panels

        + [
            FieldPanel("template_name", widget=TemplateChoiceWidget()),
        ]
    )

    def get_template(self, request, *args, **kwargs):
        return self.template_name


class AboutUsPage(MetadataPageMixin, Page):
    parent_page_types = ["website.HomePage"]
    subpage_types = []
    max_count = 1

    content_panels = (
        Page.content_panels

    )

    def get_template(self, request, *args, **kwargs):
        return "website/about_page.html"
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['board_members'] = BoardMember.objects.all()
        return context
    
class TrailsPage(MetadataPageMixin, Page):
    parent_page_types = ["website.HomePage"]
    subpage_types = []
    max_count = 1
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["map_types"] = MapCategory.objects.all()
        return context


class ProgramsPage(MetadataPageMixin, Page):
    parent_page_types = ["website.HomePage"]
    subpage_types = []
    max_count = 1

    content_panels = (
        Page.content_panels

    )

    def get_template(self, request, *args, **kwargs):
        return "website/program_page.html"
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["coaches"] = Coach.objects.all()
        return context


class Activity(Orderable):
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    activity_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("activity_photo"),
    ]


class SummerActivity(Activity):
    page = ParentalKey(
        "website.ActivitiesPage", related_name="summer_activities"
    )


class WinterActivity(Activity):
    page = ParentalKey(
        "website.ActivitiesPage", related_name="winter_activities"
    )


class ActivitiesPage(MetadataPageMixin, Page):
    parent_page_types = ["website.HomePage"]
    subpage_types = []
    max_count = 1

    content_panels = (
        Page.content_panels

        + [
            MultiFieldPanel(
                [InlinePanel("winter_activities")], heading="Winter Activities"
            ),
            MultiFieldPanel(
                [InlinePanel("summer_activities")], heading="Summer Activities"
            ),
        ]
    )

    def get_template(self, request, *args, **kwargs):
        return "website/activities_page.html"


class DayPassesPage(MetadataPageMixin, Page):
    parent_page_types = ["website.HomePage"]
    subpage_types = []
    max_count = 1

    def get_template(self, request, *args, **kwargs):
        return "website/day_pass_page.html"
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["day_passes"] = DayPassLink.objects.all()
        return context

    

# MODELS/Snippets BELOW HERE:

class BoardMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("role"),
        FieldPanel("profile_picture"),
    ]
    
    def __str__(self):
        return self.name
    
class Coach(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    profile_picture = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    biography = models.TextField(null=True, blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("title"),
        FieldPanel("profile_picture"),
        FieldPanel("biography"),
    ]

    def get_next(self):
        return Coach.objects.filter(name__gt=self.name).order_by('name').first()

    def get_prev(self):
        return Coach.objects.filter(name__lt=self.name).order_by('-name').first()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Coaches"
        ordering = ["name"]

class DayPassLink(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    panels = [
        FieldPanel("name"),
        FieldPanel("price"),
        FieldPanel("url"),
    ]

    def __str__(self):
        return self.name

class EventSession(Orderable):
    event = ParentalKey(to="website.Event", on_delete=models.CASCADE, related_name="sessions")
    date = models.DateField("Session date")
    start_time = models.TimeField("Session start time", null=True, blank=True)
    end_time = models.TimeField("Session end time", null=True, blank=True)

    panels = [
        FieldRowPanel(
            children=[
                FieldPanel("date"),
                FieldPanel("start_time"),
                FieldPanel("end_time"),
            ]
        ),
    ]

    def clean(self):
        if self.start_time and self.end_time:
            if self.start_time > self.end_time:
                raise ValidationError("Start time must be before end time.")


class Event(ClusterableModel):
    name = models.CharField(max_length=65)
    pdf = models.ForeignKey(
        "wagtaildocs.Document",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
            MultiFieldPanel(
                [
                    FieldRowPanel(
                        [
                            FieldPanel("name"),
                            FieldPanel("pdf"),
                        ],
                    )
                ],
                heading="Event Media",
            ),
            InlinePanel("sessions", max_num=15, min_num=1, label="Event Date"),
        ]
    
    def __str__(self):
        return self.name

@register_snippet
class MapCategory(models.Model):
    name = models.CharField(max_length=65)
    
    def __str__(self):
        return self.name


class Map(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(to=MapCategory, on_delete=models.RESTRICT)
    image_file = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    panel = [
        FieldRowPanel(
            children=[
                FieldPanel("category"),
                FieldPanel("image_file"),
            ]
        )
    ]
    
    def __str__(self):
        return self.title