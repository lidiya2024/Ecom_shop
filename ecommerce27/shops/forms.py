from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form_control', 'placeholder':"None of the product"}),
            'price':forms.NumberInput(attrs={'class':'form_control', 'placeholder':"Price"}),
            'description':forms.Textarea(attrs={'class':'form_control', 'placeholder':"Description"}),
            'category':forms.Select(attrs={'class':'form_control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form_control'}),
            # 'available':forms.BooleanInput(attrs={'class':'form_control', 'placeholder':"None of the product"}),
            'stock':forms.NumberInput(attrs={'class':'form_control', 'placeholder':"Stock"}),
        }




