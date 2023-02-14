from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=200, required=True)
    password = forms.CharField(
        max_length=150, widget=forms.PasswordInput, required=True
    )
    password_conf = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
        required=True,
        label="Confirm your password",
    )


class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(
        max_length=150, widget=forms.PasswordInput, required=True
    )


class FighterCreationForm(forms.Form):
    belt_choices = (
        (0, "White"),
        (1, "Blue"),
        (2, "Purple"),
        (3, "Brown"),
        (4, "Black"),
    )
    sex_choices = (("M", "Male"), ("F", "Female"))
    name = forms.CharField(max_length=150, required=True)
    weight = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    belt = forms.ChoiceField(choices=belt_choices, widget=forms.Select, required=True)
    age = forms.IntegerField(max_value=100, min_value=15, required=True)
    sex = forms.ChoiceField(choices=sex_choices, widget=forms.Select, required=True)
