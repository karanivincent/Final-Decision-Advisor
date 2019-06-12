from django import forms
from .models import Product, Accounts

class ProductForm(forms.ModelForm):

    class Meta():
        model = Product
        fields = '__all__'
        labels = {
        "s_price": "Prospective Unit Price",
        'b_price': 'Buying Price',
        }

class AccountForm(forms.ModelForm):

    class Meta():
        model = Accounts
        fields = '__all__'
        