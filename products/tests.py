from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Item
from .views import ItemDetailView


class ItemDetailViewTests(APITestCase):
    def setUp(self):
        self.valid_data = {
            "item_name": "test name",
            "item_price": 12.99,
        }
        self.url = reverse("produtc:item-detail")

    def test_get_method(self):
        item = Item.objects.create(**self.valid_data)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), )

