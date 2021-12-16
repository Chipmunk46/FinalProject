from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    item_image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Recipe
        fields = ['item_name','item_author','item_image','item_ingredients','item_instructions','item_description','item_rating','item_category']