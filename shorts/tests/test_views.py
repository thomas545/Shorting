from django.urls import reverse
from rest_framework.test import APITestCase
from ..models import ShortURL
from ..serializers import ShortURLSerializer


class TestShortURL(APITestCase):
    def setUp(self):
        self.short = ShortURL.objects.create(
            original_url="https://www.djangoproject.com/"
        )

    def test_add_new_url(self):
        url = reverse("add_short_url")
        data = {"original_url": "https://www.google.com/"}

        response = self.client.post(url, data=data)
        self.assertEqual(response.data.get("original_url"), "https://www.google.com/")

    def test_get_redirect_to_original_url(self):
        url = reverse("get_short_url", kwargs={"key": self.short.key})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)