# Page [ script_youtube/script_youtube_django/script/urls.py ]

from django.urls import path

from . import api

urlpatterns = [
    path("script_create/", api.script_create, name="script_create"),
    path("script_list/", api.script_list, name="script_list"),
    path("<uuid:pk>/script_delete/", api.script_delete, name="script_delete"),
]
