from django.db import models
from django.utils.text import slugify
from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from django import forms


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


class EventCategory(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.category}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category)
        super(EventCategory, self).save(*args, **kwargs)


class EventTags(models.Model):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.tag}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag)
        super(EventTags, self).save(*args, **kwargs)


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
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(EventTags, blank=True)

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
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('category'),
                FieldPanel('tags'),
            ])
        ], heading="Event Metadata"),
    ]
    parent_page_types = ['wagtailcore.Page']
    subpage_types = []
