from django.shortcuts import render
from django.conf import settings

from account.form import ContactForm


app_name = "home"

def main_page(request):
    return render(request, "home.html", {"form": ContactForm})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contect.html")