from rest_framework import viewsets

from images.models import Image

from api.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-created')
    serializer_class = ImageSerializer
