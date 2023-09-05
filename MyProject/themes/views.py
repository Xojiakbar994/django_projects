from django.shortcuts import render
from django.views.generic import ListView
from .models import Lessons

# Create your views here.
class LessonsView(ListView):
    def get(self, request):
        context = {}
        theme = Lessons.objects.all()
        context['lessons'] = theme

        return render(request, 'mavzu.html', context)