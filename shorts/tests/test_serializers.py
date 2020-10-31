from rest_framework.test import APITestCase
from ..models import ShortURL
from ..api.serializers import ShortURLSerializer

class TestShortURL(APITestCase):
    def setUp(self):
        self.short = ShortURL.objects.create(original_url="https://www.djangoproject.com/")

    def test_short_url_serializer_post(self):
        data = {"original_url": "https://www.djangoproject.com/"}
        serializer =  ShortURLSerializer(data=data)
        self.assertEqual(serializer.is_valid(), True)
    
    def test_short_url_serializer_get(self):
        serializer =  ShortURLSerializer(instance=self.short)
        self.assertEqual(serializer.data.get('key'), self.short.key)
