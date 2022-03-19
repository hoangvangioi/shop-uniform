from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(max_length=1000, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-2 mb-4'
            }))
        
    category_images = forms.ImageField(required=True, 
        widget=forms.FileInput(attrs={
            'class': 'form-control mt-2 mb-4'
            }))

    class Meta:
        model = Category
        fields = ("category_name", "category_images", )