from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from wagtail.snippets.models import register_snippet

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


class EventTag(models.Model):
    name = models.CharField(max_length=65)
    color = models.CharField(max_length=15, choices=ColorChoices.choices)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(EventTag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class EventCategory(models.Model):
    name = models.CharField(max_length=65)
    color = models.CharField(max_length=15, choices=ColorChoices.choices)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(EventCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    banner_image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(to=EventCategory, null=True, on_delete=models.RESTRICT)
    tags = models.ManyToManyField(to=EventTag)
    show_in_past_events = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def clean(self):
        super().clean()
        if not self.program_dates.exists():
            raise ValidationError("An event must have at least one program date.")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProgramDate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='program_dates')
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    canceled = models.BooleanField(default=False)

class BoardMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def __str__(self):
        return self.name

class Coach(models.Model):
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

    def __str__(self):
        return self.name