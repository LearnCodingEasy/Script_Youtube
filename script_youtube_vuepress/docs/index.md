
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
# Vue
```cmd
```