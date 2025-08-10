from django.shortcuts import render
from django.conf import settings


app_name = "home"

def main_page(request):
    context = {
        "restaurant_name": settings.RESTAURANT_NAME,
        "restaurant_phone": settings.RESTAURANT_CONTACT_PHONE,
        }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html", {"restaurant_name": settings.RESTAURANT_NAME})

def contact(request):
    context = {
        "restaurant_name": settings.RESTAURANT_NAME,
        "restaurant_phone": settings.RESTAURANT_CONTACT_PHONE,
        }
    return render(request, "contect.html", context)