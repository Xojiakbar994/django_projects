from django.http import HttpResponse
from django.views.generic import ListView

from .models import Countries


# Create your views here.
class CountryListView(ListView):
    # model = Countries
    def get_queryset(self):
        try:
            letter = self.request.GET["alphabet"]
            queryset = Countries.objects.filter(name__startswith=letter)
        except:
            queryset = Countries.objects.all()

        return queryset

    template_name = "country.html"
