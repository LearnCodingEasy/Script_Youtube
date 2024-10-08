
# Vite Press

```cmd
npm init vuepress script_youtube_vuepress
```

```cmd
cd script_youtube_vuepress
```

```cmd
npm install -D sass-embedded
```

```cmd
npm run docs:dev
```
* Open Docs File 📁 > Create File 📁
```
index.md
```
# Github
* Git Clone Project 📦
```cmd
git clone https://github.com/LearnCodingEasy/script_youtube.git
```

# LICENSE
* Create File 📝 [ LICENSE ]
```text
LICENSE
```
```text
MIT License
Copyright (c) 2024 Hossam Rashad
```


# Django
* Create Virtual Environment
```cmd
python -m venv script_youtube_virtual_environment
```
* Activate Virtual Environment
```cmd
script_youtube_virtual_environment\Scripts\activate
```
* Install Django
```cmd
pip install django
```
* 5 Install Django Libraries 
[ 
1 - djangorestframework | 
2 - djangorestframework-simplejwt | 
3 - django-cors-headers | 
4 - pillow 
]
```cmd
pip install djangorestframework djangorestframework-simplejwt django-cors-headers pillow
```
* Create Django Project
```cmd
django-admin startproject script_youtube_django
```
* Create Django App
```cmd
cd script_youtube_django
```
```cmd
python manage.py startapp account
```
* Setup Django File 📁 Settings
```python
# Page [script_youtube/script_youtube_django/script_youtube_django/settings.py]

from datetime import timedelta
ALLOWED_HOSTS = []
WEBSITE_URL = "http://127.0.0.1:8000"
AUTH_USER_MODEL = "account.User"
SIMPLE_JWT = {
  "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
  "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
  "ROTATE_REFRESH_TOKENS": False,
}

REST_FRAMEWORK = {
  "DEFAULT_AUTHENTICATION_CLASSES": (
      "rest_framework_simplejwt.authentication.JWTAuthentication",
  ),
  "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

CORS_ALLOWED_ORIGINS = [
  "http://localhost:5173",
  "http://localhost:5174",
]

CSRF_TRUSTED_ORIGINS = [
  "http://localhost:5173",
  "http://localhost:5174",
]

INSTALLED_APPS = [
    # ...
    # Apps
    "account",
    # Libraries
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
]

MIDDLEWARE = [
    # ...
    "corsheaders.middleware.CorsMiddleware",
    # ...
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

* Setup Django App 📦 Account
```python
# Page [ script_youtube/script_youtube_django/account/models.py ]

import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
          
    name = models.CharField(max_length=255, blank=True, default="")
    surname = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    cover = models.ImageField(upload_to="covers", blank=True, null=True)
        
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
        
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
        
    objects = CustomUserManager()
        
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
```

* Create Page 📝 [ serializers.py ] Inside App Account
```text
serializers.py
```
```python
# Page [ script_youtube/script_youtube_django/account/serializers.py ]
from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
      "id",
      "name",
      "surname",
      "email",
      "date_of_birth",
      "gender",
    )
```

* Create Page 📝[ forms.py ] Inside App Account
```text
forms.py
```
```python
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
```

* Create Page 📝 [ api.py ] Inside App Account
```text
api.py
```
```python
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
    user.is_active = False
    user.save()

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
```

* Create Page 📝[ urls.py ] Inside App Account
```text
urls.py
```
```python
# Page [ script_youtube/script_youtube_django/account/urls.py ]
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path("me/", api.me, name="me"),
    path("signup/", api.signup, name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
```

* Setup Page 📝 [ url.py ] Inside script_youtube_django
```python
# Page [ script_youtube/script_youtube_django/script_youtube_django/urls.py ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/", include("account.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

* 🛠️ Modifications To Models File
```cmd
python manage.py makemigrations
```

* 🛠️ Modifications To The Database
```cmd
python manage.py migrate
```

* 🚀 Try The Project On Your Device
```cmd
python manage.py runserver
```

# Vue
* Create Vue Project
```cmd
npm create vue@latest
```

* 11 Choose Vite [ Project name & Select a framework ]
```cmd
√ Project name: ... script_youtube_vue
√ Add TypeScript? ... [No] / Yes
√ Add JSX Support? ... [No] / Yes
√ Add Vue Router for Single Page Application development? ... No / [Yes]
√ Add Pinia for state management? ... No / [Yes]
√ Add Vitest for Unit Testing? ... [No] / Yes
√ Add an End-to-End Testing Solution? » [No]
√ Add ESLint for code quality? ... No / [Yes]
√ Add Prettier for code formatting? ... No / [Yes]
√ Add Vue DevTools 7 extension for debugging? (experimental) ... [No] / Yes

Scaffolding project in E:\Projects\script_youtube\script_youtube_vue...

Done. Now run:
  cd script_youtube_vue
  npm install
  npm run format
  npm run dev
```