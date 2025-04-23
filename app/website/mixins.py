import datetime
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel


class SeasonalFieldsMixin(models.Model):
    fall_banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    winter_banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    spring_banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    summer_banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    class Meta:
        abstract = True

    @classmethod
    def get_seasonal_panels(cls):
        return [
            MultiFieldPanel([
                FieldRowPanel([
                    FieldPanel('fall_banner_image'),
                    FieldPanel('winter_banner_image'),
                    FieldPanel('spring_banner_image'),
                    FieldPanel('summer_banner_image'),
                ]),
            ], heading='Seasonal Banner Images')
        ]

    @staticmethod
    def get_season(date=None):
        """Return the current season for the given date (or today)."""
        if date is None:
            date = datetime.date.today()

        month = date.month
        day = date.day

        if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day < 20):
            return "winter"
        elif (month == 3 and day >= 20) or (4 <= month <= 5) or (month == 6 and day < 21):
            return "spring"
        elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day < 22):
            return "summer"
        else:
            return "fall"

    def get_current_season_banner_image(self):
        """Return the banner image appropriate for the current season."""
        today = datetime.date.today()
        season = self.get_season(today)
        print(season)
        return getattr(self, f"{season}_banner_image", None)
