# Generated by Django 4.2.6 on 2023-11-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0016_rename_title_eventcategory_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventtags",
            name="color_class",
            field=models.CharField(
                choices=[
                    ("gray", "Gray"),
                    ("red", "Red"),
                    ("yellow", "Yellow"),
                    ("green", "Green"),
                    ("blue", "Blue"),
                    ("indigo", "Indigo"),
                    ("violet", "Purple"),
                    ("pink", "Pink"),
                ],
                default="gray",
                max_length=7,
            ),
        ),
    ]