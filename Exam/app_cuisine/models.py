from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Foods(models.Model):
    food_uz = models.CharField(max_length=100, verbose_name="food_uz")
    food_en = models.CharField(max_length=100, verbose_name="food_en")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")

    class Meta:
        db_table = "foods"


class Recipes(models.Model):
    recipe_uz = models.TextField(verbose_name="recipe_uz")
    recipe_en = models.TextField(verbose_name="recipe_en")

    recipe_food = models.ForeignKey(
        Foods, on_delete=models.CASCADE, verbose_name="recipe_food"
    )

    class Meta:
        db_table = "recipe"
