from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label="Name", widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter your full name",
    }))
    address = forms.CharField(required=False, label="Address", widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Enter your address",
    }))
    email = forms.EmailField(required=False, label="Email", widget=forms.EmailInput(attrs={
        "class": "form-contol",
        "placeholder": "Enter your email address",
    }))