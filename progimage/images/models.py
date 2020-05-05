from django.db import models

from django_extensions.db.fields import ShortUUIDField
from django_extensions.db.models import TimeStampedModel

from versatileimagefield.fields import VersatileImageField


class Image(TimeStampedModel):
    """
    The main model used for storing images.
    Inherits the following fields from the django_extensions helper:

      created : DateTimeField
      modified : DateTimeField

    The raw image data is meant to be stored in the `raw_image` field.

    The `height` and `width` fields are auto populated based on the image data.
    """
    uuid = ShortUUIDField(primary_key=True)
    raw_image = VersatileImageField(
        'Raw Image',
        upload_to='image_data/',
        width_field='width',
        height_field='height',
    )
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __unicode__(self):
        return self.uuid
