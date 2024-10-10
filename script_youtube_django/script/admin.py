from django.contrib import admin

from .models import ScriptVideo, ScriptAttachment, Script

admin.site.register(ScriptVideo)
admin.site.register(ScriptAttachment)
admin.site.register(Script)
