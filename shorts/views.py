from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import ShortURLForm
from .models import ShortURL

def short_create(request):
    url = ShortURL.objects.filter(original_url=request.POST.get("original_url"))
    template = "short_form.html"
    form = ShortURLForm(request.POST or None)
    context = {"form": form, "full_url": None}

    if form.errors:
        messages.error(request, str(list(form.errors.values())[0][0]))

    if url:
        full_url = str(getattr(settings, "HOST_NAME", "http://localhost:9000/")) + str(url.first().key)
        context = {"form": form, "full_url": full_url, "original_url": url.first().original_url}
    else:
        if form.is_valid():
            form.save()
            url = ShortURL.objects.filter(original_url=form.data.get("original_url"))
            full_url = str(getattr(settings, "HOST_NAME", "http://localhost:9000/")) + str(url.first().key)
            context = {"form": form, "full_url": full_url, "original_url": url.first().original_url}
    return render(request, template, context)


def redirect_to_original(request, key):
    # get url
    url = ShortURL.objects.filter(key=key)
    # redirect to url
    return redirect(url.first().original_url)


"""
for APIS
"""

# class AddShortURLView(generics.CreateAPIView):
#     """
#     Create Short URL.
#     body: {original_url: "valid url"}
#     """

#     serializer_class = ShortURLSerializer
#     queryset = ""

#     def create(self, request, *args, **kwargs):
#         # Get url if there.
#         url = ShortURL.objects.filter(original_url=request.data.get("original_url"))
#         if url:
#             # return data if url is in database
#             response = self.get_serializer(instance=url.first()).data
#         else:
#             # create short url
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             response = serializer.data
#         return Response(response)


# class ShortURLView(generics.RetrieveAPIView):
#     """
#     Redirect to original url
#     """

#     serializer_class = ShortURLSerializer
#     queryset = ShortURL.objects.all()
#     lookup_field = "key"
#     schemes = ["http", "https", "ftp", "ftps"]

#     def retrieve(self, request, *args, **kwargs):
#         url = ShortURL.objects.filter(key=kwargs.get("key"))
#         scheme = url.first().original_url.split("://")[0].lower()
#         if scheme not in self.schemes:
#             raise exceptions.ValidationError("Invalid URL", code='invalid')

#         # get the response to get original_url
#         response = super(ShortURLView, self).retrieve(request, *args, **kwargs)
#         # redirect to url
#         return redirect(response.data.get("original_url"))
