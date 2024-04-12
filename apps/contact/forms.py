from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "enter your name"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "enter your last name",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "enter your email"}
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "enter your message"}
        )
    )

    class Meta:
        model = Contact
        fields = ("name", "last_name", "email", "content")
