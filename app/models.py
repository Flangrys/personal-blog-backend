import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from app.managers import PostManager

from .validators import nickname_validation

# Create your models here.


class User(AbstractUser):
    class Meta:
        verbose_name = "users"
        verbose_name_plural = "users"

        swappable = "AUTH_USER_MODEL"
        """Allows Django auth model to swap with this custom auth model."""

    user_id = models.AutoField(primary_key=True)
    user_snowflake = models.UUIDField(
        unique=True, default=uuid.uuid4, null=False, blank=False, editable=False
    )
    user_nickname = models.CharField(
        "nickname",
        unique=False,
        max_length=30,
        blank=False,
        null=False,
        validators=[nickname_validation],
    )
    user_about = models.TextField(max_length=190, null=True, blank=True)
    is_writter = models.BooleanField(
        "writter status",
        default=False,
        help_text="Designates whether this user should be treated as a post creator.",
    )


class Tag(models.Model):
    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ["tag_name"]

    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=30, blank=False, null=False)
    tag_description = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return f"{self.tag_name} - {self.tag_description}"


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
    post_status = models.CharField(
        choices=LifecycleStatus,
        default=LifecycleStatus.RECENT,
        max_length=6,
        null=False,
        blank=False,
    )
    post_karma = models.IntegerField(default=0, blank=False, null=False)
    post_date = models.DateField(default=timezone.now, blank=False, null=False)
    post_modified_date = models.DateField(blank=True, null=True)
    post_parent = models.OneToOneField(
        "Post", on_delete=models.CASCADE, null=True, blank=True
    )
    post_tags = models.ManyToManyField(Tag, blank=True, null=True)
    post_content = models.TextField(blank=False, null=False)
    post_picture_id = models.CharField(
        unique=True, max_length=20, default="mendoza-argentina", blank=True, null=True
    )

    objects: PostManager["Post"] = PostManager()

    def __str__(self):
        return f"{self.post_author.get_username()} - {self.post_slug} @{self.post_date}"
