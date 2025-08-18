from django.db import models


class Item(models.Model):
    item_image = models.ImageField(upload_to="items/", blank=True, null=True)
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)


class Product(models.Model):
    """
    model for menu items.

    Has fields:
    - name: character field maximum 150
    - description: the text field can be empty
    - price: decimal number field maximum integers 10 after the point maximum 2 number
    - created_at: automatically filled with the current date
    """
    name = models.CharField(max_length=150, verbose_name="Name")
    description = models.TextField(blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    class __str__(self):
        return f"{self.name} | {self.created_at.strftime('%d.%m.%Y')}"