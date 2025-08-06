from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .views import ItemDetailView


class ItemDetailViewTests(APITestCase):
    def setUp(self):
        self.url = reverse("produtc:item-detail")
