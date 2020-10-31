from django.urls import path, include
from . import views

urlpatterns = [
    path("short-url/", views.CreateShortURLAPIView.as_view(), name="add_api_short_url"),
]
