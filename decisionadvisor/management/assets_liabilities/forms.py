from django import forms
from .models import Assets, Liabilities

class AssetsForm(forms.ModelForm):

    class Meta():
        model = Assets
        fields = '__all__'
        widgets = {
            'purchase_date':forms.DateInput(attrs={'type': 'date'}),

        }

class LiabilitiesForm(forms.ModelForm):

    class Meta():
        model = Liabilities
        fields = '__all__'
        widgets = {
            'due_date':forms.DateInput(attrs={'type': 'date'}),
        }
        