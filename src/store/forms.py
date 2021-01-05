from django import forms
from .models import Product, Store
from django.core.exceptions import ValidationError

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'description', 'country', 'twitter_handle', 'instagram_handle')

        # def clean(self):

        #     # function that fetches the data from the form
        #     super(StoreForm, self).clean()            
            
            
        #     name_of_store = self.cleaned_data.get('name')
        #     if Store.objects.filter(name=name_of_store).exists():
        #         return ValidationError('This store exists already, use another name')
        #         print('Store exists')
        #     return self.cleaned_data




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name_of_product', 'price', 'product_description', 'shipping_fee')