from rest_framework import viewsets

from images.models import Image


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-created')
