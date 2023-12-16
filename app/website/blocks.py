from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class VisualImageWithHeader(blocks.StructBlock):
    heading = blocks.CharBlock(label="Heading", required=True)
    text = blocks.CharBlock(label="Text", required=True)
    image = ImageChooserBlock(label="Image", required=True)
    cta_1 = blocks.StructBlock(
        [
            ("text", blocks.CharBlock(label="Text", required=False)),
            ("page", blocks.PageChooserBlock(label="Link", required=False)),
            ("external_link", blocks.URLBlock(label="URL", required=False))
        ],
        label="CTA 1",
        required=False,
    )
    cta_2 = blocks.StructBlock(
        [
            ("text", blocks.CharBlock(label="Text", required=False)),
            ("page", blocks.PageChooserBlock(label="Link", required=False)),
            ("external_link", blocks.URLBlock(label="URL", required=False))
        ],
        label="CTA 2",
        required=False,
    )



    class Meta:
        icon = "user"
        template = "blocks/visual_image_with_header.html"

class ImagesWithHeadingAndDescription(blocks.StructBlock):
    heading = blocks.CharBlock(label="Heading", required=True)
    text = blocks.CharBlock(label="Text", required=True)
    image_left = ImageChooserBlock(label="Left Image", required=True)
    image_right = ImageChooserBlock(label="Right Image", required=True)

    class Meta:
        icon = "user"
        template = "blocks/images_with_heading_and_description.html"


class DefaultCTA(blocks.StructBlock):
    heading = blocks.CharBlock(label="Heading", required=True)
    text = blocks.CharBlock(label="Text", required=True)
    cta_1 = blocks.StructBlock(
        [
            ("text", blocks.CharBlock(label="Text", required=False)),
            ("link", blocks.PageChooserBlock(label="Link", required=False)),
        ],
        label="CTA 1",
        required=False,
    )
    cta_2 = blocks.StructBlock(
        [
            ("text", blocks.CharBlock(label="Text", required=False)),
            ("link", blocks.PageChooserBlock(label="Link", required=False)),
        ],
        label="CTA 2",
        required=False,
    )

    class Meta:
        icon = "user"
        template = "blocks/default_cta.html"
