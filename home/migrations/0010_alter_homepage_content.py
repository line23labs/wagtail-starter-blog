# Generated by Django 4.1.7 on 2023-04-16 14:00

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_alter_homepage_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "hero",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "content",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "heading",
                                                    wagtail.blocks.ChoiceBlock(
                                                        choices=[
                                                            ("h1", "Heading 1"),
                                                            ("h2", "Heading 2"),
                                                            ("h3", "Heading 3"),
                                                            ("h4", "Heading 4"),
                                                        ]
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.blocks.StreamBlock(
                                                        [
                                                            (
                                                                "simple_text",
                                                                wagtail.blocks.StructBlock(
                                                                    [
                                                                        (
                                                                            "text",
                                                                            wagtail.blocks.TextBlock(
                                                                                label="Text", required=False
                                                                            ),
                                                                        )
                                                                    ],
                                                                    icon="title",
                                                                    label="Simple Text",
                                                                ),
                                                            ),
                                                            (
                                                                "styled_text",
                                                                wagtail.blocks.StructBlock(
                                                                    [
                                                                        (
                                                                            "text",
                                                                            wagtail.blocks.TextBlock(
                                                                                label="Text", required=False
                                                                            ),
                                                                        )
                                                                    ],
                                                                    icon="title",
                                                                    label="Styled Text",
                                                                ),
                                                            ),
                                                        ]
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ],
                            template="home/blocks/hero_block.html",
                        ),
                    ),
                    (
                        "contact_us",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.TextBlock()),
                                ("sub_heading", wagtail.blocks.TextBlock(label="Sub-Heading")),
                                ("photo", wagtail.images.blocks.ImageChooserBlock(required=False)),
                                ("email", wagtail.blocks.EmailBlock()),
                                ("phone_number", wagtail.blocks.CharBlock(label="Phone Number", max_length=20)),
                            ]
                        ),
                    ),
                ],
                null=True,
                use_json_field=True,
            ),
        ),
    ]
