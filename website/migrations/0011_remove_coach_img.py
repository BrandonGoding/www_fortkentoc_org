# Generated by Django 4.2.6 on 2023-11-12 23:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0010_boardmember_img"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coach",
            name="img",
        ),
    ]