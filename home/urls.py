from django.urls import path
from .views import *


urlpatterns = [
    path('about_us/', about, name='about_us'),
    path('contact/', contact, name='contact'),
    path('history/' history, name='history'),
    path('faq/' faq, name='faq'),
]