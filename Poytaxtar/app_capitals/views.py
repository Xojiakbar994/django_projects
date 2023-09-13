from django.views.generic import ListView
from django.http import HttpResponse
from django.db.models import F

from .models import Capitals


# Create your views here.
class CapitalsListView(ListView):
    # model = Capitals
    template_name = "capitals_list.html"

    def get_queryset(self):
        try:
            lang = self.request.session["lang"]
        except:
            lang = "uz"
            queryset = (
                Capitals.objects.all()
                .values("contry_" + lang, "capital_" + lang)
                .annotate(contry=F("contry_" + lang), capital=F("capital_" + lang))
            )
        return queryset


def setLanguage(request, lang):
    try:
        request.session["lang"] == lang
        return HttpResponse("ok")
    except:
        return HttpResponse("error")
