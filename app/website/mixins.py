from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel

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
    def seasonal_panels(self):
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
