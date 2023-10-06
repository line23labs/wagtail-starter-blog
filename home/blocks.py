from wagtail.blocks import CharBlock, ChoiceBlock, ListBlock, PageChooserBlock, StreamBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock

from common.blocks import CaptionedImage, ContactUsBlock, HeadingBlock, RichText


class HeroBlock(StructBlock):
    image = ImageChooserBlock()
    overlay = ChoiceBlock(
        choices=[
            ("basic", "Basic"),
            ("theme-coloured", "Theme Coloured"),
            ("theme-gradient", "Theme Coloured Gradient"),
            ("none", "None"),
        ],
        default="theme-coloured",
    )
    content = ListBlock(HeadingBlock(template="home/blocks/heading_block.html"))
    links = ListBlock(
        StructBlock([("caption", CharBlock(required=False)), ("page", PageChooserBlock(required=True))]),
        required=False,
    )

    class Meta:
        template = "home/blocks/hero_block.html"
        icon = "image"


class HomeContentStreamBlock(StreamBlock):
    hero = HeroBlock()
    contact_us = ContactUsBlock()
    richtext = RichText(template="home/blocks/rich_text.html")
    captioned_image = CaptionedImage(template="home/blocks/captioned_image.html")

    required = True
