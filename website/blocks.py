from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class BoardMemberBlock(blocks.StructBlock):
    last_name = blocks.CharBlock(label='Last Name', required=True)
    first_name = blocks.CharBlock(label='First Name', required=True)
    title = blocks.CharBlock(label='Title', required=False)
    img = ImageChooserBlock(label='Image', required=False)
    profile = blocks.CharBlock(label='Profile', required=False)


class ImagesWithHeadingAndDescription(blocks.StructBlock):
    heading = blocks.CharBlock(label='Heading', required=True)
    text = blocks.CharBlock(label='Text', required=True)
    image_left = ImageChooserBlock(label='Left Image', required=False)
    image_right = ImageChooserBlock(label='Right Image', required=False)

    class Meta:
        icon = 'user'
        form_classname = ''
        template = 'blocks/images_with_heading_and_description.html'