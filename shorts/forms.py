from django import forms
from django.core.validators import URLValidator
from .models import ShortURL


class ShortURLForm(forms.ModelForm):
    original_url = forms.CharField(
        max_length=1000, validators=[URLValidator(message="Invalid URL")]
    )

    class Meta:
        model = ShortURL
        fields = ("original_url",)
