import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from app.models import Post

# Create your views here.

log = logging.getLogger(__name__)


async def landing_view(request: HttpRequest) -> HttpResponse:

    context = {
        "author": {
            "name": "I'm Francisco M. Prieto Giorgis.",
            "desc": "Welcome to my personal blog. Built in Django and written by me using so much coffee.",
            "picture_id": "flangrys",
        },
        "posts": [
            {
                "title": post.post_title,
                "content": post.post_content,
                "status_class": post.post_status,
                "status_label": post.post_status.title(),
                "picture_id": post.post_picture_id,
            }
            async for post in Post.objects.all()
        ],
    }

    return render(request, "pages/landing_page.html", context)


def post_view(request: HttpRequest) -> HttpResponse:

    if request.user.is_staff:
        return redirect(to="/admin")

    if request.method == "GET":
        return render(
            request,
            "pages/post_page.html",
        )
