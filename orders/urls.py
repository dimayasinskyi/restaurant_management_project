from django.urls import path
from .views import *


app_name = "order"

urlpatterns = [
    path("reservation/", reservation, name="reservation")
]