from django.conf import settings
from rest_framework import serializers
from .models import ShortURL
from .validators import URLValidator


class ShortURLSerializer(serializers.ModelSerializer):
    original_url = serializers.CharField(validators=[URLValidator()])
    full_url = serializers.SerializerMethodField(read_only=True, required=False)

    def get_full_url(self, obj):
        return (
            str(getattr(settings, "HOST_NAME", "http://localhost:9000/"))
            + "short-url/"
            + str(obj.key)
        )

    class Meta:
        model = ShortURL
        fields = (
            "original_url",
            "key",
            "full_url",
        )
        read_only_fields = (
            "key",
            "full_url",
        )
