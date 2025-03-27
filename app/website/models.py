from django.core.exceptions import ValidationError
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from .fields import TemplateChoiceWidget


class HomePage(Page):
    max_count = 1
    subpage_types = [
        'website.UpcomingListingPage',
        'website.LegacyPage',
        'website.AboutUsPage',
        'website.ProgramsPage',
    ]

class UpcomingListingPage(Page):
    parent_page_types = ['website.HomePage']
    subpage_types = ['website.EventPage']
    max_count = 2

class EventSession(Orderable):
    page = ParentalKey("website.EventPage", related_name="sessions")
    date = models.DateField("Session date")
    start_time = models.TimeField("Session start time", null=True, blank=True)
    end_time = models.TimeField("Session end time", null=True, blank=True)
    
    panels = [
        FieldRowPanel(
            children=
            [
            FieldPanel('date'),
            FieldPanel('start_time'),
            FieldPanel('end_time'),
            ]
        ),
    ]

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError("Start time must be before end time.")

    def __str__(self):
        return self.title

class EventPage(Page):
    parent_page_types = ['website.UpcomingListingPage']
    subpage_types = []
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    pdf = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    details = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('details'),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('banner_image'),
                        FieldPanel('main_image'),
                        FieldPanel('pdf'),
                    ],
                )
            ],
            heading="Event Media"
        ),
        InlinePanel("sessions", max_num=10, min_num=1, label="Event Date"),
    ]

    def __str__(self):
        return self.title
    
#################### OLD PAGES ####################
class LegacyPage(Page):
    subpage_types = ['website.HomePage']
    template_name = models.CharField(max_length=255, default='default_template.html')
    
    content_panels = Page.content_panels + [
        FieldPanel('template_name', widget=TemplateChoiceWidget()),
    ]
    
    def get_template(self, request, *args, **kwargs):
        return self.template_name


class BoardMember(Orderable):
    page = ParentalKey("website.AboutUsPage", related_name="board_members")
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('role'),
        FieldPanel('profile_picture'),
    ]

class AboutUsPage(Page):
    parent_page_types = ['website.HomePage']
    subpage_types = []
    max_count = 1
    
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("board_members", max_num=10, min_num=1, label="Board Member")],
            heading="Board Members",
        ),
    ]
    
    def get_template(self, request, *args, **kwargs):
        return 'website/about_page.html'
    

class Coach(Orderable):
    page = ParentalKey("website.ProgramsPage", related_name="coaches")
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    profile_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    biography = models.TextField(null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('title'),
        FieldPanel('profile_picture'),
        FieldPanel('biography')
    ]

class ProgramsPage(Page):
    parent_page_types = ['website.HomePage']
    subpage_types = []
    max_count = 1

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("coaches", max_num=10, min_num=1, label="Program Coaches")],
            heading="Program Coaches",
        ),
    ]

    def get_template(self, request, *args, **kwargs):
        return 'website/program_page.html'
