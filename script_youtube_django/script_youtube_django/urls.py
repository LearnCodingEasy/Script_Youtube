# Page [ script_youtube/script_youtube_django/script_youtube_django/urls.py ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/", include("account.urls")),
    path("api/scripts/", include("script.urls")),
    path("api/tasks/", include("task.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
