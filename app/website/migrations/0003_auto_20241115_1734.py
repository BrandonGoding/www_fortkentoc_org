# Generated by Django 4.2.6 on 2024-11-15 22:34

from django.db import migrations
from django.utils.text import slugify


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0002_auto_20241115_1730"),
    ]

    def create_event_tags(apps, schema_editor):
        EventTag = apps.get_model('website', 'EventTag')

        tags = [
            ("High School Race", "gray"),
            ("Middle School Race", "red"),
            ("Invitational", "yellow"),
            ("Board Elections", "green"),
            ("Social Event", "blue"),
            ("Rental Shop", "purple"),
            ("Membership Drive", "pink"),
            ("Hosted By UMFK", "gray"),
            ("Championship Event", "red"),
            ("Fundraiser", "yellow"),
            ("Ski Lessons", "green"),
            ("Ladies Only", "blue"),
            ("Poker Run", "purple"),
            ("Biathlon", "pink"),
            ("Nordic", "gray"),
        ]

        for name, color in tags:
            EventTag.objects.create(
                name=name,
                color=color,
                slug=slugify(name),
            )

    def delete_event_tags(apps, schema_editor):
        EventTag = apps.get_model('website', 'EventTag')

        tag_names = [
            "High School Race",
            "Middle School Race",
            "Invitational",
            "Board Elections",
            "Social Event",
            "Rental Shop",
            "Membership Drive",
            "Hosted By UMFK",
            "Championship Event",
            "Fundraiser",
            "Ski Lessons",
            "Ladies Only",
            "Poker Run",
            "Biathlon",
            "Nordic",
        ]

        EventTag.objects.filter(name__in=tag_names).delete()

    operations = [
        migrations.RunPython(create_event_tags, delete_event_tags),
    ]