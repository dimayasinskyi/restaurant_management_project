from django.shortcuts import render
from django.conf import settings

from account.form import ContactForm
from account.models import Contact


app_name = "home"

def main_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
    else:
        form = ContactForm()

    return render(request, "home.html", {"form": form})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contect.html")