from django.db import models
from django.contrib.auth.models import User


class OrderStatusChoices(models.TextChoices):
    """
    Order status selection class for the Order model.

    Options to choose from:
    - Pending
    - Processing
    - Shipped
    - Delivered
    - Cancelled
    - Refunded
    """
    PENDING = "pending", "Pending"
    PROCESSING = "processing", "Processing"
    SHIPPED = "shipped", "Shipped"
    DELIVERED = "delivered", "Delivered"
    CANCELLED = "cancelled", "Cancelled"
    REFUNDED = "refunded", "Refunded"


class Order(models.Model):
    """
    Has fields:
    - customer: will be associated with the User model type many-to-one cascade delete
    - order_items: will be associated with the Item model many-to-many relationship (related name "items")
    - total_amount: should contain the total amount that fills the signal (optional) 
    - status: dropdown list based on class OrderStatusChoices (default is processing)

    Method:
    - __str__: returns full customer name and total amount (f"{self.customer.get_full_name()} | {self.total_amount}")
    """
    customer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="orders", verbose_name="Customer")
    order_items = models.ManyToManyField(to="products.Item", related_name="items", verbose_name="Items")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Total amount")
    status = models.CharField(
        max_length=50, 
        choices=OrderStatusChoices.choices, 
        default=OrderStatusChoices.PROCESSING, 
        verbose_name="Status"
        )

    class Meta:
        ordering = ["status"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"
    
    def __str__(self):
        return f"{self.customer.get_full_name()} | {self.total_amount}"
