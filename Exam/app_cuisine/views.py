from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Foods, Recipes
from django.db.models import F
from django.http import HttpResponse


# Create your views here.
class FoodsView(ListView):
    # models = Foods
    template_name = "cuisine/food.html"

    # def get_queryset(self):
    #     return Foods.objects.all()

    def get_queryset(self):
        try:
            lang = self.request.session["lang"]
        except:
            lang = "uz"
            self.request.session["lang"] = "uz"

        queryset = (
            Foods.objects.all()
            .values("id", "food_" + lang)
            .annotate(food=F("food_" + lang))
        )
        return queryset


class RecipesView(ListView):
    template_name = "cuisine/recipe.html"

    def get_queryset(self):
        try:
            pk = self.request.GET["recipe_food"]
        except:
            pk = 1

        try:
            lang = self.request.session["lang"]
        except:
            lang = "uz"
            self.request.session["lang"] = "uz"

        queryset = (
            Recipes.objects.filter(recipe_food=pk)
            .values("recipe_food", "recipe_" + lang)
            .annotate(recipe=F("recipe_" + lang))
        )
        return queryset


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Foods
    template_name = "cuisine/food-new.html"
    fields = ("food_uz", "food_en", "recipe_uz", "recipe_en")
    success_url = "/users/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def setLanguage(request, lang):
    request.session["lang"] = lang
    return HttpResponse("OK")
