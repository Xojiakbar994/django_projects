from django.views.generic import ListView
from django.http import HttpResponse
from django.db.models import F

from .models import Districts


# Create your views here.
class DistrictsListView(ListView):
    # model = Districts

    @property
    def get_queryset(self):
        try:
            lang = self.request.session["lang"]
        except:
            lang = "uz"
            queryset = (
                Districts.objects.all()
                .values("district_name_" + lang)
                .annotate(district_name=F("district_name_" + lang))
            )
        return queryset

    template_name = "index.html"


def setLanguage(request, lang):
    try:
        request.session["lang"] = lang
        return HttpResponse("ok")
    except:
        return HttpResponse("error")
