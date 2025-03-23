from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.models import Page, Orderable
from wagtail.snippets.models import register_snippet
from .fields import TemplateChoiceWidget

COLOR_CODES = {
    "gray": {
        "100": "#f3f4f6",
        "200": "#e5e7eb",
        "800": "#1f2937",
        "900": "#111827",
    },
    "red": {
        "100": "#fde8e8",
        "200": "#fbd5d5",
        "800": "#9b1c1c",
        "900": "#771d1d",
    },
    "yellow": {
        "100": "#fdf6b2",
        "200": "#fce96a",
        "800": "#723b13",
        "900": "#633112",
    },
    "green": {
        "100": "#def7ec",
        "200": "#bcf0da",
        "800": "#03543f",
        "900": "#014737",
    },
    "blue": {
        "100": "#e1effe",
        "200": "#c3ddfd",
        "800": "#1e429f",
        "900": "#233876",
    },
    "purple": {
        "100": "#e5edff",
        "200": "#cddbfe",
        "800": "#42389d",
        "900": "#362f78",
    },
    "pink": {
        "100": "#fce8f3",
        "200": "#fad1e8",
        "800": "#99154b",
        "900": "#751a3d",
    },
}


class ColorChoices(models.TextChoices):
    GRAY = "gray", "Gray"
    RED = "red", "Red"
    YELLOW = "yellow", "Yellow"
    GREEN = "green", "Green"
    BLUE = "blue", "Blue"
    PURPLE = "purple", "Purple"
    PINK = "pink", "Pink"

    @staticmethod
    def color_code(color: str) -> str:
        return COLOR_CODES[color]


class TagCategoryBase(models.Model):
    name = models.CharField(max_length=65)
    color = models.CharField(max_length=15, choices=ColorChoices.choices)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(TagCategoryBase, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

@register_snippet
class EventCategory(TagCategoryBase):
    pass

@register_snippet
class EventTag(TagCategoryBase):
    pass

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
    
class EventPage(Page):
    parent_page_types = ['website.UpcomingListingPage']
    subpage_types = []
    tags = models.ManyToManyField(EventTag, blank=True)
    categories = models.ForeignKey(EventCategory, blank=True, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

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
    page = ParentalKey("website.AboutUsPage", related_name="coaches")
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
