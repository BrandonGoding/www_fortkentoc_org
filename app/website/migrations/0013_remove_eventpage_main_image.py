# Generated by Django 4.2.6 on 2025-04-27 21:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0012_remove_eventpage_fall_banner_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventpage",
            name="main_image",
        ),
    ]
