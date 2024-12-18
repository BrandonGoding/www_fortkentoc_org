# Generated by Django 4.2.6 on 2024-11-15 22:40
from django.db import migrations
from django.utils.text import slugify
from datetime import datetime
from pytz import UTC


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0004_remove_event_url_event_slug_alter_programdate_event"),
    ]

    def add_events(apps, schema_editor):
        Event = apps.get_model("website", "Event")  # Replace with your Event model
        EventCategory = apps.get_model("website", "EventCategory")
        EventTag = apps.get_model("website", "EventTag")
        ProgramDate = apps.get_model("website", "ProgramDate")

        EVENTS = [
            {
                "title": "Seasonal Ski Rentals",
                "program_dates": [
                    {"date": "2023-11-18", "start_time": "13:00", "end_time": "15:00"},
                    {"date": "2023-12-03", "start_time": "13:00", "end_time": "15:00"},
                ],
            },
            {
                "title": "Welcome Winter Celebration",
                "program_dates": [
                    {"date": "2023-12-02", "start_time": "17:00", "end_time": "20:00"}
                ],
            },
            {
                "title": "USBA Nationals",
                "program_dates": [
                    {"date": "2024-03-21", "start_time": "09:00"},
                    {"date": "2024-03-22", "start_time": "09:00"},
                    {"date": "2024-03-23", "start_time": "09:00"},
                    {"date": "2024-03-24", "start_time": "09:00"},
                ],
                "category": "US Biathlon Association",
                "tags": ["Championship Event"],
                "show_in_past_events": True,
                "url": "/events/usba-nationals/",
            },
            {
                "title": "U15 Biathlon Camp",
                "program_dates": [
                    {"date": "2024-07-22"},
                    {"date": "2024-07-23"},
                    {"date": "2024-07-24"},
                    {"date": "2024-07-25"},
                ],
                "category": "Training Camp",
                "tags": ["Biathlon"],
                "banner_image_url": "/website/img/biathlon_camp/campbanner.jpg",
                "url": "/events/2024-biathlon-camp/",
            },
            # Add more events here as needed
        ]

        for event_data in EVENTS:
            category = None
            if "category" in event_data:
                category = EventCategory.objects.filter(
                    name=event_data["category"]
                ).first()

            tags = []
            if "tags" in event_data:
                tags = EventTag.objects.filter(
                    name__in=event_data["tags"]
                )

            event = Event.objects.create(
                title=event_data["title"],
                category=category,
                show_in_past_events=event_data.get("show_in_past_events", False),
            )

            if tags:
                event.tags.set(tags)

            for date_data in event_data["program_dates"]:
                start_time = datetime.strptime(date_data.get("start_time", "00:00"), "%H:%M").time()
                end_time = date_data.get("end_time")
                if end_time:
                    end_time = datetime.strptime(end_time, "%H:%M").time()
                ProgramDate.objects.create(
                    event=event,
                    date=datetime.strptime(date_data["date"], "%Y-%m-%d").replace(tzinfo=UTC),
                    start_time=start_time,
                    end_time=end_time,
                    canceled=date_data.get("cancelled", False),
                )

    def remove_events(apps, schema_editor):
        Event = apps.get_model("website", "Event")
        Event.objects.all()

    operations = [
        migrations.RunPython(add_events, remove_events),
    ]
