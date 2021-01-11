from django import forms
from .models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'state', 'country']