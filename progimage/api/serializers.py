from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    """Serializes Person instances"""
    raw_image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )

    class Meta:
        model = Image
        fields = (
            'uuid', 'raw_image',
        )
