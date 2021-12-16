from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['item_name', 'item_author', 'item_description', 'item_ingredients', 'item_instructions', 'item_image',
                  'item_rating','item_category']
