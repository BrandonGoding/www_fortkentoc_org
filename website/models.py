from django.db import models
from django.utils.text import slugify
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


class BoardMember(models.Model):
    last_name = models.CharField(max_length=26)
    first_name = models.CharField(max_length=26)
    title = models.CharField(max_length=16, blank=True)
    img = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

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
    img = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

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
    img_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.author}"


class Event(Page):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    teaser = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"
