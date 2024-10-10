# Page [ script_youtube/script_youtube_django/script/forms.py ]

from django.forms import ModelForm

from .models import ScriptAttachment, ScriptVideo, Script


class ScriptForm(ModelForm):
    class Meta:
        model = Script
        fields = (
            "title",
            "list_of_sources_urls",
            "list_of_shots",
            "list_of_Paragraphs",
            "list_of_fonts_urls",
        )


class AttachmentForm(ModelForm):
    class Meta:
        model = ScriptAttachment
        fields = ("image",)


class VideoForm(ModelForm):
    class Meta:
        model = ScriptVideo
        fields = ("video",)
