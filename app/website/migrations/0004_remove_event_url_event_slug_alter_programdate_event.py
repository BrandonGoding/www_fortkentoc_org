# Generated by Django 4.2.6 on 2024-11-15 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0003_auto_20241115_1734"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="url",
        ),
        migrations.AddField(
            model_name="event",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programdate",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="program_dates",
                to="website.event",
            ),
        ),
    ]