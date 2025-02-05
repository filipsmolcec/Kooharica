from django import forms
from .models import *

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['author', 'date_posted', 'date_updated']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        field = '__all__'
        exclude = ['author', 'date_posted', 'date_updated']