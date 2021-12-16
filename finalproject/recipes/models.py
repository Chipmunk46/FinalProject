from django.db import models


# Create your models here.
class Recipe(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_author = models.CharField(max_length=500)
    item_image = models.ImageField(default='recipepic.jpg', upload_to='recipe_pictures')
    item_ingredients = models.CharField(max_length=20000)
    item_instructions = models.CharField(max_length=50000)
    item_description = models.CharField(max_length=50000)
    item_rating = models.IntegerField()
    item_category = models.CharField(max_length=500,choices=(('Chinese','Chinese'),('Indian','Indian'),('Mexican','Mexican'),('American','American')),default="None")

class SavedRecipes(models.Model):
    item_user = models.CharField(max_length=500)
    item_recipeid = models.CharField(max_length=500)