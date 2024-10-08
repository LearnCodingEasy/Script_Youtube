# Page [ script_youtube/script_youtube_django/account/api.py ]
from django.conf import settings


from django.contrib.auth.forms import PasswordChangeForm

from django.core.mail import send_mail

from django.http import JsonResponse

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)


from .forms import SignupForm

from .models import User


from .serializers import UserSerializer


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):

    data = request.data
    message = "success"

    form = SignupForm(
        {
            "name": data.get("name"),
            "surname": data.get("surname"),
            "email": data.get("email"),
            "date_of_birth": data.get("date_of_birth"),
            "gender": data.get("gender"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    if form.is_valid():
        user = form.save()
        user.is_active = True
        user.save()
        print(message)
        return JsonResponse({"message": message, "email_sent": True}, safe=False)
    else:
        message = form.errors.as_json()

    print(message)

    return JsonResponse({"message": message}, safe=False)


@api_view(["GET"])
def me(request):
    return JsonResponse(
        {
            "id": request.user.id,
            "name": request.user.name,
            "surname": request.user.surname,
            "email": request.user.email,
            "date_of_birth": request.user.date_of_birth,
            "gender": request.user.gender,
        }
    )
