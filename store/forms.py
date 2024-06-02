from django import forms
from .models import Product, Image

class ProductForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = ['name', 'price', 'brand', 'categories']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['url', 'color']
