from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProductForm(forms.ModelForm):
    product_name = forms.CharField(max_length=1000, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-2 mb-4'
            }))
        
    product_images = forms.ImageField(required=True, 
        widget=forms.FileInput(attrs={
            'class': 'form-control mt-2 mb-4'
            }))
        
    description = forms.CharField(required=True, 
        widget=CKEditorUploadingWidget(
        attrs={
            'class': 'form-control mt-2 mb-4'
            }
    ))

    price = forms.IntegerField(required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control mt-2 mb-4'
            }))

    stock = forms.IntegerField(required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control mt-2 mb-4'
            }))
            
    category = forms.ModelChoiceField(required=True,
        queryset = Category.objects.all(),
        label = 'Chọn danh mục sản phẩm',
        widget=forms.Select(attrs={
            'class': 'form-control mt-2 mb-4',
            }))

    class Meta:
        model = Product
        fields = ("product_name", "description", "price", "product_images", "stock", "category")