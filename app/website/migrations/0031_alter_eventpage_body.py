# Generated by Django 4.2.6 on 2023-11-18 23:10

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0030_eventpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    (
                        "default_cta",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(
                                        label="Heading", required=True
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        label="Text", required=True
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.PageChooserBlock(
                                        label="CTA Link", required=False
                                    ),
                                ),
                                (
                                    "link_2",
                                    wagtail.blocks.PageChooserBlock(
                                        label="CTA Link 2", required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "left_header_paragraph_two_image_right",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(
                                        label="Heading", required=True
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        label="Text", required=True
                                    ),
                                ),
                                (
                                    "image_left",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Left Image", required=True
                                    ),
                                ),
                                (
                                    "image_right",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Right Image", required=True
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]