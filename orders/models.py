from django.db import models

from products.models import Item


class Order(models.Model):
    customer
    items
    status
