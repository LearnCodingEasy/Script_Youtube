# Page [ script_youtube/script_youtube_django/script/forms.py ]

from django.forms import ModelForm

from .models import ScriptAttachment, ScriptVideo, Script


class ScriptForm(ModelForm):
    class Meta:
        model = Script
        fields = (
            "script_status",
            "is_private",
            "title",
            "list_of_sources_urls",
            "list_of_shots",
            "list_of_examples",
            "list_of_paragraphs",
            "list_of_fonts_urls",
            "list_of_colors",
            "list_of_musics",
            "list_of_videos_background",
            "list_of_images",
            "list_of_icons",
            "list_of_visual_effects",
            "list_of_transitions",
            "list_of_sound_effects",
            "script",
        )


class AttachmentForm(ModelForm):
    class Meta:
        model = ScriptAttachment
        fields = ("image",)


class VideoForm(ModelForm):
    class Meta:
        model = ScriptVideo
        fields = ("video",)
