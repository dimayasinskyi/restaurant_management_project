from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Item
from .views import ItemDetailView


class ItemDetailViewTests(APITestCase):
    def setUp(self):
        self.valid_data = {
            "item_name": "test name",
            "item_price": 
        }
        self.url = reverse("produtc:item-detail")


