from django.contrib import admin

# Register your models here.

from .models import Board, List

# admin.site.register(ScriptVideo)
admin.site.register(List)
admin.site.register(Board)
