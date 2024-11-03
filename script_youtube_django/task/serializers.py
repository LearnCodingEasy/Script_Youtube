# Page [ script_youtube/script_youtube_django/task/serializers.py ]

from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Board, List, Task


# All
class BoardSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = (
            "id",
            "title",
            "background",
            # Automatic
            "created_by",
            "created_at",
            "created_at_formatted",
        )


class ListSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    # board = BoardSerializer(read_only=True, many=True)
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    class Meta:
        model = List
        fields = (
            "id",
            "title",
            "board",
            "position",
            # Automatic
            "created_by",
            "created_at",
            "created_at_formatted",
        )


# Single


class BoardDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = (
            "id",
            "title",
            # Automatic
            "created_by",
            "created_at",
            "created_at_formatted",
        )


class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "task_status",
            "is_private",
            "title",
            "list_of_item_number",
            # Automatic
            "created_by",
            "created_at",
            "created_at_formatted",
        )


class TaskDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "task_status",
            "is_private",
            "title",
            "list_of_item_number",
            # Automatic
            "created_by",
            "created_at",
            "created_at_formatted",
        )
