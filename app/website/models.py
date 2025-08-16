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
from wagtailmetadata.models import MetadataPageMixin
from datetime import date
from wagtail.snippets.models import register_snippet
import uuid
from modelcluster.models import ClusterableModel


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
        return (
            Coach.objects.filter(name__gt=self.name).order_by("name").first()
        )

    def get_prev(self):
        return (
            Coach.objects.filter(name__lt=self.name).order_by("-name").first()
        )

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
    event = ParentalKey(
        to="website.Event", on_delete=models.CASCADE, related_name="sessions"
    )
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
