# Page [ script_youtube/script_youtube_django/script/models.py ]

import uuid
from django.utils.timesince import timesince
from django.conf import settings
from django.db import models
from account.models import User


class ScriptAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="script_attachments")
    created_by = models.ForeignKey(
        User, related_name="script_attachments", on_delete=models.CASCADE
    )

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ""


class ScriptVideo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to="Script_videos")
    created_by = models.ForeignKey(
        User, related_name="script_videos", on_delete=models.CASCADE
    )

    def get_video(self):
        if self.video:
            return settings.WEBSITE_URL + self.video.url
        else:
            return ""


class Script(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TASKS = "Tasks"
    DONE = "Done"
    IN_MAKING = "In Making"
    scriptStatusList = [
        ("TASKS", "Tasks"),
        ("DONE", "Done"),
        ("IN_MAKING", "In Making"),
    ]
    #
    script_status = models.CharField(
        max_length=50, choices=scriptStatusList, default=TASKS, blank=True
    )
    # Boolean
    is_private = models.BooleanField(default=False)
    title = models.TextField(blank=True, null=True)
    list_of_sources_urls = models.JSONField(default=list, blank=True, null=True)
    list_of_shots = models.JSONField(default=list, blank=True, null=True)
    list_of_examples = models.JSONField(default=list, blank=True, null=True)
    list_of_paragraphs = models.JSONField(default=list, blank=True, null=True)
    list_of_fonts_urls = models.JSONField(default=list, blank=True, null=True)
    list_of_colors = models.JSONField(default=list, blank=True, null=True)
    list_of_musics = models.JSONField(default=list, blank=True, null=True)
    list_of_videos_background = models.JSONField(default=list, blank=True, null=True)
    list_of_images = models.JSONField(default=list, blank=True, null=True)
    list_of_icons = models.JSONField(default=list, blank=True, null=True)
    list_of_visual_effects = models.JSONField(default=list, blank=True, null=True)
    list_of_transitions = models.JSONField(default=list, blank=True, null=True)
    list_of_sound_effects = models.JSONField(default=list, blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    # 🖼️ Image
    attachments = models.ManyToManyField(ScriptAttachment, blank=True)
    # 🎥 Video
    videos = models.ManyToManyField(ScriptVideo, blank=True)
    # Automatic
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="scripts", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return
