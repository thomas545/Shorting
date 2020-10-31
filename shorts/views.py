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


def api_documentation(request):
    return render(request, 'api_docs.html', context={})