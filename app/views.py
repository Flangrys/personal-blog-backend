from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.models import Post

# Create your views here.


def landing_view(request: HttpRequest) -> HttpResponse:

    all_posts = [post for post in Post.objects.all()]

    return render(
        request,
        "landing_page.html",
        {
            "page_author_title": "I'm Francisco M. Prieto Giorgis.",
            "page_author_desc": "Welcome to my personal blog. Built in Django and written by me using so much coffee.",
            "page_posts": all_posts,
        },
    )
