# Generated by Django 4.2.6 on 2023-11-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0010_eventtags_alter_coach_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventpage",
            name="tags",
            field=models.ManyToManyField(blank=True, to="website.eventtags"),
        ),
    ]