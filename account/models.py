from django.db import models 
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    The model is created to represent user data.

    Has fields:
    - user: one-to-one relationship to the user model
    - name: The character field has a limit of 255 characters must contain the full name (optional)
    - email: email address field (optional)
    - phone_number: The character field has a limit of 16 characters (optional)

    Method:
    - __str__: return field "name"
    """
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name="User")
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    email = models.EmailFIeld(blank=True, null=True, verbose_name="Email")
    phone_number = models.CharField(max_length=16, blank=True, null=True, verbose_name="Phone")

    class Meta:
        ordering = ["-name"]
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.name