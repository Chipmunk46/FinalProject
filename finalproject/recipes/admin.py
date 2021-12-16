from django.contrib import admin
from .models import Recipe
from .models import SavedRecipes
# Register your models here.
admin.site.register(Recipe)
admin.site.register(SavedRecipes)