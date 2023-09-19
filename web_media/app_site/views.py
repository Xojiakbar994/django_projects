from django.views.generic import ListView
from .models import Themes, Plans


# Create your views here.
class ThemesView(ListView):
    # models = Themes
    template_name = "theme.html"

    def get_queryset(self):
        return Themes.objects.all()


class PlansView(ListView):
    template_name = "plan.html"

    def get_queryset(self):
        try:
            pk = self.request.GET["plan_theme"]
        except:
            pk = 1

        queryset = Plans.objects.filter(plan_theme=pk).values("plan", "plan_text")
        return queryset
