# Generated by Django 4.2.6 on 2023-11-15 00:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0004_rename_img_boardmember_photo"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Event",
        ),
    ]