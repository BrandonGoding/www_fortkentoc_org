# Generated by Django 4.2.6 on 2023-11-15 00:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0003_boardmember_img"),
    ]

    operations = [
        migrations.RenameField(
            model_name="boardmember",
            old_name="img",
            new_name="photo",
        ),
    ]