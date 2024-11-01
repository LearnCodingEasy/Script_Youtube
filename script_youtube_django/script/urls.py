# Page [ script_youtube/script_youtube_django/script/urls.py ]

from django.urls import path

from . import api

urlpatterns = [
    path("script_create/", api.script_create, name="script_create"),
    path("script_list/", api.script_list, name="script_list"),
    path(
        "script_list/<uuid:id>/",
        api.script_list_dashboard,
        name="script_list_dashboard",
    ),
    path(
        "script_list/script_detail/<uuid:pk>/", api.script_detail, name="script_detail"
    ),
    path("script_list/script_edit/<uuid:pk>/", api.script_edit, name="script_edit"),
    path(
        "script_list/script_delete/<uuid:pk>/", api.script_delete, name="script_delete"
    ),
]
