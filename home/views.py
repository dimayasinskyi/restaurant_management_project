from django.shortcuts import render
from django.conf import settings

from .models import RestaurantLocationModel


app_name = "home"

def main_page(request):
    return render(request, "home.html" {"restaurant_location": RestaurantLocationModel.objects.all()})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contect.html")