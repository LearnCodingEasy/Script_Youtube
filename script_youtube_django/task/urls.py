# Page [ script_youtube/script_youtube_django/task/urls.py ]

from django.urls import path

from . import api

urlpatterns = [
    # Board
    path("board_create/", api.board_create, name="board_create"),
    path("board_list/<uuid:id>/", api.board_list, name="board_list"),
    # List
    path("list_create/", api.list_create, name="list_create"),
    path("list_list/<uuid:board_id>/", api.list_list, name="list_list"),
    #
    path("task_create/", api.task_create, name="task_create"),
    path("task_list/", api.task_list, name="task_list"),
    # path(
    #     "script_list/script_detail/<uuid:pk>/", api.script_detail, name="script_detail"
    # ),
    # path("script_list/script_edit/<uuid:pk>/", api.script_edit, name="script_edit"),
    # path(
    #     "script_list/script_delete/<uuid:pk>/", api.script_delete, name="script_delete"
    # ),
]
