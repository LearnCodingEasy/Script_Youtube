# Page [ script_youtube/script_youtube_django/task/api.py ]

from django.db.models import Q
from django.http import JsonResponse

from django.shortcuts import get_object_or_404

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from account.models import User
from account.serializers import UserSerializer

from .forms import BoardForm, ListForm, TaskForm
from .models import Board, List, Task
from .serializers import (
    BoardSerializer,
    BoardDetailSerializer,
    ListSerializer,
    TaskSerializer,
    TaskDetailSerializer,
)

#
from rest_framework.response import Response


@api_view(["POST"])
def board_create(request):
    # Handling the Board Form and Attachment Form
    form = BoardForm(request.POST)

    # Proceed with the Task form if it's valid
    if form.is_valid():
        board = form.save(commit=False)
        board.created_by = request.user
        board.save()

        # Increment user's board count
        user = request.user
        user.task_count = user.task_count + 1
        user.save()

        # Serialize the Task and return as JSON response
        serializer = BoardSerializer(board)
        return JsonResponse(serializer.data, status=201)  # HTTP 201 Created
    else:
        # If form validation fails, return error response
        # errors = form.errors.as_json()
        errors = {
            "board_errors": form.errors,
        }
        return JsonResponse({"error": errors}, status=400)


# board List For User
@api_view(["GET"])
def board_list(request, id):
    user = User.objects.get(pk=id)
    boards = Board.objects.filter(created_by_id=id)
    board_serializer = BoardSerializer(boards, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse(
        {
            "boards": board_serializer.data,
            "user": user_serializer.data,
        },
        safe=False,
    )


@api_view(["POST"])
def list_create(request):
    # Handling the List Form and Attachment Form
    form = ListForm(request.POST)

    # Proceed with the Task form if it's valid
    if form.is_valid():
        new_list = form.save(commit=False)
        new_list.created_by = request.user
        new_list.save()

        # Increment user's board count
        user = request.user

        user.save()

        # Serialize the Task and return as JSON response
        serializer = ListSerializer(new_list)
        return JsonResponse(serializer.data, status=201)  # HTTP 201 Created
    else:
        # If form validation fails, return error response
        # errors = form.errors.as_json()
        errors = {
            "list_errors": form.errors,
        }
        return JsonResponse({"error": errors}, status=400)


# board List For User
@api_view(["GET"])
def list_list(request, board_id):

    # الحصول على الـ Board
    board = Board.objects.get(pk=board_id)
    # استرجاع جميع القوائم المرتبطة بالـ Board
    lists = List.objects.filter(board_id=board_id)

    # تسلسل البيانات
    board_serializer = BoardSerializer(board)
    list_serializer = ListSerializer(lists, many=True)

    # إرجاع البيانات كـ JSON
    return JsonResponse(
        {
            "lists": list_serializer.data,
            "board": board_serializer.data,
        },
        safe=False,
    )


@api_view(["POST"])
def task_create(request):
    # Handling the Task Form and Attachment Form
    form = TaskForm(request.POST)

    # Proceed with the Task form if it's valid
    if form.is_valid():
        task = form.save(commit=False)
        task.created_by = request.user
        task.save()

        # Increment user's Task count
        user = request.user
        user.task_count = user.task_count + 1
        user.save()

        # Serialize the Task and return as JSON response
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data, status=201)  # HTTP 201 Created
    else:
        # If form validation fails, return error response
        # errors = form.errors.as_json()
        errors = {
            "task_errors": form.errors,
        }
        return JsonResponse({"error": errors}, status=400)


# Tasks List
@api_view(["GET"])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)
