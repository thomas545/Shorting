from rest_framework import generics
from rest_framework.response import Response
from .serializers import ShortURLSerializer
from ..models import ShortURL


class CreateShortURLAPIView(generics.CreateAPIView):
    """
    Create Short URL.
    body: {original_url: "valid url"}
    """

    serializer_class = ShortURLSerializer
    queryset = ""

    def create(self, request, *args, **kwargs):
        # Get url if there.
        url = ShortURL.objects.filter(original_url=request.data.get("original_url"))
        if url:
            # return data if url is in database
            response = self.get_serializer(instance=url.first()).data
        else:
            # create short url
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = serializer.data
        return Response(response)
