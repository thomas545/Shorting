from django.urls import path, include
from . import views

urlpatterns = [
    path("short-url/", views.AddShortURLView.as_view(), name="add_short_url"),
    path("short-url/<str:key>/", views.ShortURLView.as_view(), name="get_short_url"),
]
