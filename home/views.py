from django.shortcuts import render
from django.conf import settings


app_name = "home"

def about(request):
    return render(request, "about.html", {"restaurant_name": settings.RESTAURANT_NAME})