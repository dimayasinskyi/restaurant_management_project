from django.urls import path
from .views import *


urlpatterns = [
    path('about_us', about, name="about_us")
]