# Generated by Django 4.2.6 on 2023-12-10 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("website", "0058_daypasssquarelink_fee"),
    ]

    operations = [
        migrations.AddField(
            model_name="daypasspage",
            name="show_support_image_1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Support Image 1",
            ),
        ),
        migrations.AddField(
            model_name="daypasspage",
            name="show_support_image_2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Support Image 2",
            ),
        ),
    ]