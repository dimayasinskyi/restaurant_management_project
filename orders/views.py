from django.shortcuts import render


def reservation(request):
    return render(request, "reservations.html")
