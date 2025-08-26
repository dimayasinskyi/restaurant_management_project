from django.shortcuts import render
from django.conf import settings

from account.form import ContactForm
from account.models import Contact
from products.models import Item
from orders.models import Order

app_name = "home"

def main_page(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
    else:
        form = ContactForm()

    if request.GET.get("find"):
        items_menu = Item.objects.filter(item_name__contains=request.GET["find"])
    else:
        items_menu = None

    contect = {
        "form": form,
        "map_key": settings.GOOGLE_MAP_API_KEY,
        "items_menu": items_menu,
        "total_qty": ,
    }
    return render(request, "home.html", contect)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contect.html")