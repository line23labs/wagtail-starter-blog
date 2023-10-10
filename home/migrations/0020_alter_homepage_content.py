# Generated by Django 4.2.6 on 2023-10-10 07:21

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('overlay', wagtail.blocks.ChoiceBlock(choices=[('basic', 'Basic'), ('theme-coloured', 'Theme Coloured'), ('theme-gradient', 'Theme Coloured Gradient'), ('none', 'None')])), ('content', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('h1', 'Heading 1'), ('h2', 'Heading 2'), ('h3', 'Heading 3'), ('h4', 'Heading 4')])), ('text', wagtail.blocks.StreamBlock([('simple_text', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Text', required=False))], icon='title', label='Simple Text')), ('styled_text', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Text', required=False))], icon='title', label='Styled Text'))]))], template='home/blocks/heading_block.html'))), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=True))]), required=False)), ('button', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False)), ('style', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary')], required=False))], required=False, template='home/blocks/hero_block_button.html'))])), ('contact_us', wagtail.blocks.StructBlock([('heading', wagtail.blocks.TextBlock()), ('sub_heading', wagtail.blocks.TextBlock(label='Sub-Heading')), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('email', wagtail.blocks.EmailBlock()), ('phone_number', wagtail.blocks.CharBlock(label='Phone Number', max_length=20))])), ('richtext', wagtail.blocks.StructBlock([('rich_text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'embed']))], template='home/blocks/rich_text.html')), ('captioned_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 800px')), ('caption', wagtail.blocks.TextBlock(help_text='Optional: caption text to appear below the image', required=False)), ('caption_link', wagtail.blocks.URLBlock(help_text='Optional: external link to appear below the image', required=False)), ('caption_label', wagtail.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False))], template='home/blocks/captioned_image.html')), ('our_stack', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=True)), ('content', wagtail.blocks.RichTextBlock(required=True)), ('button', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False)), ('style', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary')], required=False))], required=False))]))], null=True, use_json_field=True),
        ),
    ]
