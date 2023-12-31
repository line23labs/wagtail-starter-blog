# Generated by Django 4.1.7 on 2023-05-19 07:54

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_articlepage_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "rich_text",
                        wagtail.blocks.StructBlock(
                            [("rich_text", wagtail.blocks.RichTextBlock())],
                            features=["h2", "h3", "h4", "bold", "italic", "ol", "ul", "link"],
                        ),
                    )
                ],
                null=True,
                use_json_field=True,
            ),
        ),
    ]
