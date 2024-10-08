# Page [ script_youtube/script_youtube_django/account/forms.py ]

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "name",
            "surname",
            "email",
            "date_of_birth",
            "gender",
            "password1",
            "password2",
        )
