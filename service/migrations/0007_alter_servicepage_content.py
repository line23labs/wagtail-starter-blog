# Generated by Django 4.1.7 on 2023-05-18 08:42

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0006_alter_servicepage_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicepage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "hero",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock(required=False)),
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
                            ]
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
                    ("richtext", wagtail.blocks.RichTextBlock(template="service/blocks/richtext.html")),
                    (
                        "anchor",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "anchor_id",
                                    wagtail.blocks.CharBlock(
                                        help_text="The unique indentifier for this anchor", required=True
                                    ),
                                ),
                                (
                                    "name",
                                    wagtail.blocks.CharBlock(
                                        help_text="Used on the navigation link (if used)", required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "services",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.TextBlock(required=True)),
                                (
                                    "services",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("heading", wagtail.blocks.CharBlock(required=True)),
                                                ("description", wagtail.blocks.RichTextBlock()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                null=True,
                use_json_field=True,
            ),
        ),
    ]
