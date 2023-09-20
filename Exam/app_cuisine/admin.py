from django.contrib import admin
from .models import Foods, Recipes


# Register your models here.
# admin.site.register(Todos)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ("id", "food")
    list_filter = ["food", "user"]

    admin.site.register(Foods)


class RecipesAdmin(admin.ModelAdmin):
    list_display = ("id", "recipe")
    list_filter = ["recipe", "user"]

    admin.site.register(Recipes)
