# Page [ script_youtube/script_youtube_django/task/forms.py ]

from django.forms import ModelForm

from .models import Board, List, Card, Task


class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ("title", "background")


class ListForm(ModelForm):
    class Meta:
        model = List
        fields = (
            "title",
            "board",
            "position",
        )


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ("title", "description", "list", "position")


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("task_status", "is_private", "title", "list_of_item_number")
