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


# _______________________
# user_ids = [request.user.id]

# for user in request.user.friends.all():
#     user_ids.append(user.id)

# posts = Post.objects.filter(created_by_id__in=list(user_ids))

# trend = request.GET.get("trend", "")

# if trend:
#     posts = posts.filter(body__icontains="#" + trend).filter(is_private=False)

# serializer = PostSerializer(posts, many=True)

# return JsonResponse(serializer.data, safe=False)


# @api_view(["GET"])
# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     user = post.created_by

#     user_serializer = UserSerializer(user)

#     post_serializer = PostDetailSerializer(post)
#     return JsonResponse(
#         {
#             "post": post_serializer.data,
#             "user": user_serializer.data,
#         },
#         safe=False,
#     )


# @api_view(["GET"])
# def post_list_profile(request, id):

#     user = User.objects.get(pk=id)
#     posts = Post.objects.filter(created_by_id=id)

#     # user = get_object_or_404(User, pk=id)

#     # posts = Post.objects.filter(created_by_id=id)

#     # if not request.user in user.friends.all():
#     #     posts = posts.filter(is_private=False)

#     posts_serializer = PostSerializer(posts, many=True)
#     user_serializer = UserSerializer(user)

#     can_send_friendship_request = True

#     if request.user in user.friends.all():
#         can_send_friendship_request = False

#     check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
#         created_by=user
#     )
#     check2 = FriendshipRequest.objects.filter(created_for=user).filter(
#         created_by=request.user
#     )

#     if check1 or check2:
#         can_send_friendship_request = False

#     return JsonResponse(
#         {
#             "posts": posts_serializer.data,
#             "user": user_serializer.data,
#             "can_send_friendship_request": can_send_friendship_request,
#         },
#         safe=False,
#     )
