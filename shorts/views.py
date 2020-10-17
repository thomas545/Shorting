from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics, exceptions
from rest_framework.response import Response
from .serializers import ShortURLSerializer
from .models import ShortURL


class AddShortURLView(generics.CreateAPIView):
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


class ShortURLView(generics.RetrieveAPIView):
    """
    Redirect to original url
    """

    serializer_class = ShortURLSerializer
    queryset = ShortURL.objects.all()
    lookup_field = "key"
    schemes = ["http", "https", "ftp", "ftps"]

    def retrieve(self, request, *args, **kwargs):
        url = ShortURL.objects.filter(key=kwargs.get("key"))
        scheme = url.first().original_url.split("://")[0].lower()
        if scheme not in self.schemes:
            raise exceptions.ValidationError("Invalid URL", code='invalid')

        # get the response to get original_url
        response = super(ShortURLView, self).retrieve(request, *args, **kwargs)
        # redirect to url
        return redirect(response.data.get("original_url"))
