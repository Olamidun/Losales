from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django import forms


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    email = forms.EmailField()
    # password = forms.CharField() 
    # confirm_password = forms.CharField()

    class Meta:
        model = Account

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']