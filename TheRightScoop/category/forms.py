from django import forms
from .models import Category   


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category     
        fields = [
            'name',
            'cat_desc',
            'cat_img',
            'cat_parent',
            'is_active',
        ]
