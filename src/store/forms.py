from django import forms
from .models import Product, Store


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'description', 'country', )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name_of_product', 'price', 'product_description')