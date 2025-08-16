from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.ImageField(upload_to="items/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)

