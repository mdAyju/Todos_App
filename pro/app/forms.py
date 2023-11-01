from django import forms
from app.models import DataModel



class DataForm(forms.ModelForm):
    class Meta:
        model=DataModel
        fields =['name','locality','mobile','state','zipcode']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
        }