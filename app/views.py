import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from app.models import Post

# Create your views here.

log = logging.getLogger(__name__)


def landing_view(request: HttpRequest) -> HttpResponse:

    post = Post.objects.get_most_recent()[0]

    context = {
        "author": {
            "name": post.post_author.user_nickname,
            "about": post.post_author.user_about,
            "picture_id": "flangrys",
        },
        "post": {
            "title": post.post_title,
            "description": post.post_description,
            "status_class": post.post_status,
            "status_label": post.post_status.title(),
            "picture_id": post.post_picture_id,
        },
    }

    return render(request, "pages/landing.html", context)


def post_view(request: HttpRequest, **kwargs) -> HttpResponse:
    params = kwargs.get("slug")

    posts: Post = None

    if params:
        posts = Post.objects.get(post_slug=params)

    return render(request, "pages/posts.html", {"all_posts": posts})
