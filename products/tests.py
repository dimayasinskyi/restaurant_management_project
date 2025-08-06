from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Item
from .serializers import ItemSerializer
from .views import ItemDetailView


class ItemDetailViewTests(APITestCase):

    def setUp(self):
        self.valid_data = {
            "item_name": "test name",
            "item_price": 12.99,
        }
        self.item = Item.objects.create(**self.valid_data)
        self.serializer = ItemSerializer(self.item)
        self.url = reverse("product:item-detail", kwargs={"id": self.item.id})

    def test_get_method(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.serializer.data)

    def test_put_method(self):
        put_data = {
            "item_name": "test name2",
            "item_price": 10,
        }
        response = self.client.put(self.url, data=put_data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['item_name'], put_data['item_name'])
        self.assertEqual(response.data['item_price'], put_data['item_price'])

    def test_patch_method(self):
        patch_data = {
            "item_name": "test name2",
        }
        response = self.client.patch(self.url, data=patch_data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['item_name'], patch_data['item_name'])
        self.assertEqual(response.data['item_price'], self.valid_data['item_price'])

    def test_delete_method(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"delete": f"deleted item by id {self.item.id}"})
    
    def test_get_method_404_error(self):
        response = self.client.get(reverse("product:item-detail", kwargs={"id": 100}))
        self.assertEqual(response.status_code, 404)

    def test_update_data_400_error(self):
        invalid_data = {
            "item_name": 123,
            "item_price": "abc"
        }
        response = self.client.put(self.url, data=invalid_data, format="json")
        self.assertEqual(response.status_code, 400)