from django.shortcuts import render
from django.conf import settings


def about(request):
    return render(request, "about.html", {"restaurant": settings.RESTAURANT_NAME})