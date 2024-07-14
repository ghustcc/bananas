from django import forms
from .models import Lots

class LotForm(forms.ModelForm):
    class Meta:
        model = Lots
        fields = ('nome_titular', 'local', 'hectares')