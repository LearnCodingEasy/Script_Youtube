# Page [ script_youtube/script_youtube_django/task/models.py ]

import uuid
from django.utils.timesince import timesince
from django.conf import settings
from django.db import models
from account.models import User


class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    background = models.CharField(max_length=100, default="#FFFFFF")
    # Automatic
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="boards", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return


class List(models.Model):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board, related_name="lists", on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
    # Automatic
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="created_lists", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    list = models.ForeignKey(Board, related_name="cards", on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
    # Automatic
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="created_cards", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return


class Task(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TASKS = "Tasks"
    DONE = "Done"
    IN_MAKING = "In Making"
    taskStatusList = [
        ("TASKS", "Tasks"),
        ("DONE", "Done"),
        ("IN_MAKING", "In Making"),
    ]
    #
    task_status = models.CharField(
        max_length=50, choices=taskStatusList, default=TASKS, blank=True
    )
    # Boolean
    is_private = models.BooleanField(default=False)
    title = models.TextField(blank=True, null=True)
    list_of_item_number = models.IntegerField(default=0)
    # Automatic
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return
