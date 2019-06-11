from django import forms
from .models import Assets, Liabilities

class AssetsForm(forms.ModelForm):

    class Meta():
        model = Assets
        fields = ('name', 'value', 'PurchaseDate')

class LiabilitiesForm(forms.ModelForm):

    class Meta():
        model = Liabilities
        fields = ('name', 'amount', 'DueDate', 'StartDate')
        