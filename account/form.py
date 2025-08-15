from django import forms

from .models import Feetback


class Feetback(forms.ModelForm):
    """
    Form for leaving comments on menu items.

    Has only a text field.
    """
    def Meta:
        model = Feetback
        fields = ["text"]