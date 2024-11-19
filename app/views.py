from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def landing_view(request: HttpRequest) -> HttpResponse:

    return render(request, "landing_page.html", {
        "page_author_title": "I'm Francisco M. Prieto Giorgis.",
        "page_author_desc": "Welcome to my personal blog. Built in Django and written by me using so much coffee.",
    })
