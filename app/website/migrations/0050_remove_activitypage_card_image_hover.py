# Generated by Django 4.2.6 on 2023-11-20 03:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0049_alter_activitypage_banner_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="activitypage",
            name="card_image_hover",
        ),
    ]