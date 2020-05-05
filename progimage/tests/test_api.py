import os

from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework import status
from rest_framework.test import APITestCase

from images.models import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def here(p):
    " Helper to construct relative paths for testing "
    return os.path.join(BASE_DIR, 'tests', p)


class ImageAPITests(APITestCase):
    def test_post(self):
        url = reverse('image-list')
        with open(here('img.jpg'), 'rb') as fp:
            data = {'raw_image': fp}
            response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(Image.objects.get().uuid, response.json()['uuid'])

    def test_get(self):
        with open(here('img.jpg'), 'rb') as fp:
            upload = SimpleUploadedFile(name='img.jpg', content=fp.read(), content_type='image/jpeg')
            img = Image.objects.create(raw_image=upload)
        url = reverse('image-list')
        response = self.client.get("{}{}/".format(url, img.uuid), format='json')
        self.assertEqual(response.json()['uuid'], img.uuid)
