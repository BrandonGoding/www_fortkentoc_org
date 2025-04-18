# Generated by Django 5.0.3 on 2025-03-28 23:02

import django.db.models.deletion
import wagtailmetadata.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        (
            "website",
            "0003_aboutuspage_search_image_activitiespage_search_image_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="DayPassesPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "search_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Search image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                wagtailmetadata.models.WagtailImageMetadataMixin,
                "wagtailcore.page",
                models.Model,
            ),
        ),
    ]
