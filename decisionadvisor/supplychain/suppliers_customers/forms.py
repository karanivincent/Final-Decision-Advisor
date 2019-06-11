from django import forms 
from .models import Customers, Suppliers

class SupplierForm(forms.ModelForm):

    class Meta():
        model=Suppliers
        fields = '__all__'
       

class CustomerForm(forms.ModelForm):

    class Meta():
        model=Customers
        fields = '__all__'
        

