from django import forms
from .models import Assets, Liabilities

class AssetsForm(forms.ModelForm):

    class Meta():
        model = Assets
        fields = '__all__'

class LiabilitiesForm(forms.ModelForm):

    class Meta():
        model = Liabilities
        fields = '__all__'
        