# Page [ script_youtube/script_youtube_django/script/api.py ]

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

from .forms import ScriptForm, AttachmentForm, VideoForm
from .models import Script
from .serializers import ScriptSerializer, ScriptDetailSerializer

#
from rest_framework.response import Response


@api_view(["POST"])
def script_create(request):
    # Handling the Script Form and Attachment Form
    form = ScriptForm(request.POST)
    attachment_form = AttachmentForm(request.POST, request.FILES)
    video_form = VideoForm(request.POST, request.FILES)
    # First, process the attachment form if it's valid
    attachment = None
    if attachment_form.is_valid():
        attachment = attachment_form.save(commit=False)
        attachment.created_by = request.user
        attachment.save()
    # First, process the Video form if it's valid
    video = None
    if video_form.is_valid():
        video = video_form.save(commit=False)
        video.created_by = request.user
        video.save()

    # Proceed with the Script form if it's valid
    if form.is_valid():
        script = form.save(commit=False)
        script.created_by = request.user
        script.save()

        # If there's an attachment, associate it with the script
        if attachment:
            script.attachments.add(attachment)
        # If there's an Video, associate it with the script
        if video:
            script.videos.add(video)

        # Increment user's script count
        user = request.user
        # user.scripts_count += 1
        user.save()

        # Serialize the script and return as JSON response
        serializer = ScriptSerializer(script)
        return JsonResponse(serializer.data, status=201)  # HTTP 201 Created
    else:
        # If form validation fails, return error response
        # errors = form.errors.as_json()
        errors = {
            "script_errors": form.errors,
            "attachment_errors": attachment_form.errors,
            "video_errors": video_form.errors,
        }
        return JsonResponse({"error": errors}, status=400)


# Scripts List
@api_view(["GET"])
def script_list(request):
    scripts = Script.objects.all()
    serializer = ScriptSerializer(scripts, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["DELETE"])
def script_delete(request, pk):
    script = Script.objects.filter(created_by=request.user).get(pk=pk)
    script.delete()
    return JsonResponse({"message": "script deleted"})


@api_view(["GET"])
def script_detail(request, pk):
    script = Script.objects.get(pk=pk)
    user = script.created_by

    user_serializer = UserSerializer(user)

    script_serializer = ScriptDetailSerializer(script)
    return JsonResponse(
        {
            "script": script_serializer.data,
            "user": user_serializer.data,
        },
        safe=False,
    )


@api_view(["GET", "PUT"])
def script_edit(request, pk):
    # Get the script object to update
    script = get_object_or_404(Script, pk=pk, created_by=request.user)

    if request.method == "GET":
        # Serialize the script data and return as JSON
        serializer = ScriptSerializer(script)
        return JsonResponse(serializer.data, status=200)  # HTTP 200 OK

    elif request.method == "PUT":
        # Handling the Script Form, Attachment Form, and Video Form
        form = ScriptForm(request.data, instance=script)
        attachment_form = AttachmentForm(request.data, request.FILES)
        video_form = VideoForm(request.data, request.FILES)

        # Update the attachment if valid
        attachment = None
        if attachment_form.is_valid():
            attachment = attachment_form.save(commit=False)
            attachment.created_by = request.user
            attachment.save()

        # Update the video if valid
        video = None
        if video_form.is_valid():
            video = video_form.save(commit=False)
            video.created_by = request.user
            video.save()

        # Proceed with updating the script if valid
        if form.is_valid():
            script = form.save()

            # Associate updated attachment and video with the script
            if attachment:
                script.attachments.add(attachment)
            if video:
                script.videos.add(video)

            # Serialize the updated script and return as JSON response
            serializer = ScriptSerializer(script)
            return JsonResponse(serializer.data, status=200)  # HTTP 200 OK
        else:
            # If form validation fails, return error response
            errors = {
                "script_errors": form.errors,
                "attachment_errors": attachment_form.errors,
                "video_errors": video_form.errors,
            }
            return JsonResponse({"error": errors}, status=400)
