from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def landing_view(request: HttpRequest) -> HttpResponse:

    return render(request, "app/templates/onboarding.html", {
        "page_headline": "Hola mundo!",
        "page_headline_desc": "Este es mi blog personal ;)",
    })