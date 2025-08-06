from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Item
from .serializers import ItemSerializer
from .views import ItemDetailView


class ItemDetailViewTests(APITestCase):
    def setUp(self):
        valid_data = {
            "item_name": "test name",
            "item_price": 12.99,
        }
        item = Item.objects.create(**valid_data)
        self.serializers = ItemSerializer(item)
        self.url = reverse("produtc:item-detail", kwargs=item.id)

    def test_get_method(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.serializers.data)

    def test_put_method(self):
        put_data = {
            "item_name": "test name2",
            "item_price": 10,
        }
        response = self.client.put(self.url, data=put_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['item_name'], put_data['item_name'])
        self.assertEqual(response['item_price'], put_data['item_price'])

    def test_patch_method(self):
        patch_data = {
            "item_name": "test name2",
        }
        response = self.client.patch(self.url, data=patch_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['item_name'], patch_data['item_name'])
        self.assertEqual(response['item_price'], self.valid_data['item_price'])

    def test_patch_method(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 200)
    
