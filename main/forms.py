from django import forms
from .models import *

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'instructions', 'cook_time_minutes',
                  'author', 'date_posted', 'date_updated']
        exclude = ['author', 'date_posted', 'date_updated']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        field = ['title', 'content', 'author',
                 'date_posted', 'date_updated']
        exclude = ['author', 'date_posted', 'date_updated']