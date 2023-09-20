from django.urls import path
from .views import FoodsView, RecipesView, FoodCreateView, setLanguage

urlpatterns = [
    path("setLang/<str:lang>", setLanguage),
    path("recipes", RecipesView.as_view(), name="recipes"),
    path("new", FoodCreateView.as_view(), name="food-new"),
    path("", FoodsView.as_view(), name="foods"),
]
