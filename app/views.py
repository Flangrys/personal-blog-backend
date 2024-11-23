from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.models import Post

# Create your views here.


def landing_view(request: HttpRequest) -> HttpResponse:

    all_posts = [post for post in Post.objects.all()]

    context = {
        "author": {
            "name": "I'm Francisco M. Prieto Giorgis.",
            "desc": "Welcome to my personal blog. Built in Django and written by me using so much coffee.",
            "picture_id": "flangrys",
        },
        "post": {
            "title": "Example post.",
            "content": "Lorem impsu",
            "status_class": "new",
            "status_label": "New",
            "picture_id": "mendoza-argentina",
        },
    }

    return render(request, "pages/landing_page.html", context)
