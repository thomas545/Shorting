from django.db import models
from django.utils.translation import gettext_lazy as _
from .utils import generate_random_key


class ShortURL(models.Model):
    original_url = models.TextField(verbose_name=_("Original Url"))
    key = models.CharField(max_length=50, unique=True, default=generate_random_key)
    created = models.DateTimeField(auto_now_add=True)
