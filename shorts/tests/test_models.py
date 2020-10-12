from rest_framework.test import APITestCase
from ..models import ShortURL

class TestShortURL(APITestCase):
    def test_short_url(self):
        short = ShortURL.objects.create(original_url="https://www.djangoproject.com/")
        self.assertEqual(short.__str__(), short.key)
