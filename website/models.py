from django.db import models
from django.utils.text import slugify
from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


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
    slug = models.SlugField(max_length=50, null=True)
    img = models.ImageField(upload_to='coaches', blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

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


class EventPage(Page):
    class EventLocationChoices(models.TextChoices):
        LODGE = 'fkoc_lodge', 'Fort Kent Outdoor Center Lodge'
        WAX_BUILDING = 'wax_building', 'Fort Kent Outdoor Center Wax Building'
        STADIUM = 'stadium', 'Fort Kent Outdoor Center Stadium'

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    teaser = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=EventLocationChoices.choices)
    body = RichTextField(blank=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Banner Image"
    )

    def __str__(self):
        return f"{self.title}"

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('location'),
            FieldRowPanel([
                FieldPanel('date'),
                FieldPanel('start_time'),
                FieldPanel('end_time'),
            ]),
            ], heading="Event Information"
        ),
        MultiFieldPanel([
            FieldPanel('banner_image'),
            FieldPanel('teaser'),
            FieldPanel('body'),
        ], heading="Event Description"),
    ]

    parent_page_types = ['wagtailcore.Page']
    subpage_types = []
