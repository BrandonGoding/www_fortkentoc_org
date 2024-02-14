from django.db import models

from django.utils.text import slugify


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

    color_class = models.CharField(
        max_length=7, default=ColorChoices.GRAY, choices=ColorChoices.choices
    )

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


class Event(models.Model):
    class EventLocationChoices(models.TextChoices):
        LODGE = "fkoc_lodge", "Fort Kent Outdoor Center Lodge"
        WAX_BUILDING = "wax_building", "Fort Kent Outdoor Center Wax Building"
        STADIUM = "stadium", "Fort Kent Outdoor Center Stadium"
        PARKING_LOT = "parking_lot", "Fort Kent Outdoor Center Parking Lot"

    name = models.CharField(max_length=255)
    teaser = models.CharField(max_length=200)
    location = models.CharField(
        max_length=50, choices=EventLocationChoices.choices
    )

    category = models.ForeignKey(
        EventCategory, on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField(EventTag, blank=True)

    def __str__(self):
        return f"{self.name}"


