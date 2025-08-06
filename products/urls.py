from django.urls import path

from .views import *


app_name = "product"

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('items/<int:id>/', ItemDetailView.as_view(), name='item-detail'),
]