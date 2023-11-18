import datetime

from django import forms
from django.db import models
from django.utils.text import slugify
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page, Orderable

from website.blocks import ImagesWithHeadingAndDescription, DefaultCTA

COLOR_CODES = {
        "gray": {
            "100": "#f3f4f6",
            "200": "#e5e7eb",
            "800": "#1f2937",
            "900": "#111827"
        },
        "red": {
            "100": "#fde8e8",
            "200": "#fbd5d5",
            "800": "#9b1c1c",
            "900": "#771d1d"
        },
        "yellow": {
            "100": "#fdf6b2",
            "200": "#fce96a",
            "800": "#723b13",
            "900": "#633112"
        },
        "green": {
            "100": "#def7ec",
            "200": "#bcf0da",
            "800": "#03543f",
            "900": "#014737"
        },
        "blue": {
            "100": "#e1effe",
            "200": "#c3ddfd",
            "800": "#1e429f",
            "900": "#233876"
        },
        "purple": {
            "100": "#e5edff",
            "200": "#cddbfe",
            "800": "#42389d",
            "900": "#362f78"
        },
        "pink": {
            "100": "#fce8f3",
            "200": "#fad1e8",
            "800": "#99154b",
            "900": "#751a3d"
        }
    }


class BoardMember(models.Model):
    last_name = models.CharField(max_length=26)
    first_name = models.CharField(max_length=26)
    title = models.CharField(max_length=16, blank=True)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('last_name'),
        FieldPanel('first_name'),
        FieldPanel('title'),
        FieldPanel('photo'),
    ]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def web_display_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Board Member"
        verbose_name_plural = "Board Members"


class Coach(models.Model):
    last_name = models.CharField(max_length=26)
    first_name = models.CharField(max_length=26)
    profile = models.TextField()
    title = models.CharField(max_length=32, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True, help_text="Leave blank to auto-generate slug.")
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('last_name'),
                FieldPanel('first_name'),
            ]),
            FieldPanel('title'),
        ], heading="Name & Title"),
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('photo'),
            FieldPanel('profile'),
        ], heading="Profile"),
    ]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"coach-{self.first_name}-{self.last_name}")
        super(Coach, self).save(*args, **kwargs)

    def web_display_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Coach"
        verbose_name_plural = "Coaches"


class Testimonial(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    testimonial = models.TextField()
    img = models.ImageField(upload_to='testimonials', blank=True)

    def __str__(self):
        return f"{self.author}"


class EventListingPage(Page):
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # NEED TO INCORPORATE live().child_of(self) TO FILTER OUT PAST EVENTS
        context['events'] = EventDate.objects.filter(date__gte=datetime.date.today(), page__live=True).order_by('date')
        context['categories'] = EventCategory.objects.all().order_by('name')
        context['tags'] = EventTag.objects.all().order_by('name')
        return context


class NameAndSlugModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class ColorChoices(models.TextChoices):
        GRAY = "gray", "Gray"
        RED = "red", "Red"
        YELLOW = "yellow", "Yellow"
        GREEN = "green", "Green"
        BLUE = "blue", "Blue"
        PURPLE = "purple", "Purple"
        Pink = "pink", "Pink"

    color_class = models.CharField(max_length=7, default=ColorChoices.GRAY, choices=ColorChoices.choices)

    @property
    def color_code(self):
        return COLOR_CODES[self.color_class]

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(NameAndSlugModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class EventCategory(NameAndSlugModel):
    pass


class EventTag(NameAndSlugModel):
    pass


class EventPage(Page):
    class EventLocationChoices(models.TextChoices):
        LODGE = 'fkoc_lodge', 'Fort Kent Outdoor Center Lodge'
        WAX_BUILDING = 'wax_building', 'Fort Kent Outdoor Center Wax Building'
        STADIUM = 'stadium', 'Fort Kent Outdoor Center Stadium'

    teaser = models.CharField(max_length=200)
    location = models.CharField(max_length=50, choices=EventLocationChoices.choices)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('default_cta', DefaultCTA()),
        ('left_header_paragraph_two_image_right', ImagesWithHeadingAndDescription()),
    ], use_json_field=True, blank=True, null=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Banner Image"
    )
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True)
    tags = ParentalManyToManyField(EventTag)

    def __str__(self):
        return f"{self.title}"

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('location'),
            InlinePanel("dates", max_num=20, min_num=1, label="Event Date"),
        ], heading="Event Information"
        ),
        MultiFieldPanel([
            FieldPanel('banner_image'),
            FieldPanel('teaser'),
            FieldPanel('body'),
        ], heading="Event Description"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('category', widget=forms.RadioSelect),
                FieldPanel('tags', widget=forms.CheckboxSelectMultiple),
            ])
        ], heading="Event Metadata"),
    ]
    parent_page_types = ['website.EventListingPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['upcoming_events'] = EventDate.objects.filter(date__gte=datetime.date.today(), page__live=True).exclude(page_id=self.pk).order_by('date')
        return context


class EventDate(Orderable):
    page = ParentalKey(EventPage, on_delete=models.CASCADE, null=True, related_name='dates')
    date = models.DateField("Event Date")
    start_time = models.TimeField("Start Time")
    end_time = models.TimeField("End Time", blank=True, null=True)

    panels = [
        FieldPanel('date'),
        FieldPanel('start_time'),
        FieldPanel('end_time'),
    ]
