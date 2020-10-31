from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.short_create, name="add_short_url"),
    path("<str:key>/", views.redirect_to_original, name="get_short_url"),
    path('api/docs/', views.api_documentation, name="api_docs"),
]


urlpatterns += [
    path("api-v1/", include('shorts.api.urls')),
]