from django.utils import timezone
from django.db import models


# Create your models here.

class User(models.Model):
    class Meta:
        ordering = ["user_registration_date"]

    user_id = models.AutoField(primary_key=True)
    user_nickname = models.CharField(max_length=30, blank=False, null=False)
    user_full_name = models.CharField(max_length=70, blank=False, null=False)
    user_email = models.EmailField(blank=False, null=False)
    user_registration_date = models.DateField(default=timezone.now, blank=False, null=False)

class Tag(models.Model):
    class Meta:
        ordering = ["tag_name"]

    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=30, blank=False, null=False)
    tag_description = models.CharField(max_length=70, blank=True, null=True)


class LifecycleStatus(models.TextChoices):
    """Represents what stage of the lifecycle the blog post is in."""

    RECENT = "recent", "Recent"
    EDITED = "edited", "Edited"
    OUTDATED = "old", "Old"


class Post(models.Model):
    class Meta:
        ordering = ["post_title"]

    post_id = models.AutoField(primary_key=True)
    post_author = models.OneToOneField(User, on_delete=models.PROTECT)
    post_title = models.CharField(max_length=70, blank=False, null=False)
    post_description = models.CharField(max_length=300, blank=False, null=False)
    post_slug = models.SlugField(max_length=40, blank=False, null=False)
    post_pinned = models.BooleanField(default=False)
    post_status = models.CharField(choices=LifecycleStatus, default=LifecycleStatus.RECENT, max_length=6, null=False, blank=False)
    post_karma = models.IntegerField(default=0, blank=False, null=False)
    post_date = models.DateField(default=timezone.now, blank=False, null=False)
    post_modified_date = models.DateField(blank=True, null=True)
    post_parent = models.OneToOneField("Post", on_delete=models.CASCADE, null=True)
    post_tags = models.ManyToManyField(Tag)
    post_content = models.TextField(blank=False, null=False)
