from django.shortcuts import render
from django.conf import settings


app_name = "home"

def main_page(request):
    return render(request, "home.html", {"restaurant_name": settings.RESTAURANT_NAME})

def about(request):
    return render(request, "about.html", {"restaurant_name": settings.RESTAURANT_NAME})

def contect(request):
    return render(request, "contect.html", {"restaurant_name": settings.RESTAURANT_NAME})