# Page [ script_youtube/script_youtube_django/script/serializers.py ]

from rest_framework import serializers

from account.serializers import UserSerializer

from .models import ScriptAttachment, ScriptVideo, Script


class ScriptAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptAttachment
        fields = (
            "id",
            "get_image",
        )


class ScriptVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptVideo
        fields = (
            "id",
            "get_video",
        )


class ScriptSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = ScriptAttachmentSerializer(read_only=True, many=True)
    videos = ScriptVideoSerializer(read_only=True, many=True)

    class Meta:
        model = Script
        fields = (
            "id",
            "title",
            "list_of_sources_urls",
            "list_of_shots",
            "list_of_Paragraphs",
            "list_of_fonts_urls",
            "created_by",
            "created_at_formatted",
            "attachments",
            "videos",
        )


class ScriptDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = ScriptAttachmentSerializer(read_only=True, many=True)
    videos = ScriptVideoSerializer(read_only=True, many=True)

    class Meta:
        model = Script
        fields = (
            "id",
            "title",
            "list_of_sources_urls",
            "list_of_shots",
            "list_of_Paragraphs",
            "list_of_fonts_urls",
            "created_by",
            "created_at_formatted",
            "attachments",
            "videos",
        )
