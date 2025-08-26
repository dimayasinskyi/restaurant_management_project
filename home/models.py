from django.db import models


class RestaurantLocationModel(models.Model):
    """
    Model for storing information about the location of a restaurant.

    Has fields:
    - phone: field characters maximum 16
    - address: text field
    - city: field characters maximum 189
    - state: field characters maximum 14 (optionally)
    - zip_code: field characters maximum 10
    - created_at: automatically filled with the current time
    """
    phone = models.CharField(max_length=16, verbose_name="Phone")
    address = models.TextField(verbose_name="Address")
    city = models.CharField(max_length=189, verbose_name="City")
    state = models.CharField(max_length=14, blank=True, verbose_name="State")
    zip_code = models.CharField(max_length=10, verbose_name="Zip")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        ordering = ["city"]
        verbose_name = "Restaurant Location"
        verbose_name_plural = "Restaurants Location"

    def __str__(self):
        return self.city