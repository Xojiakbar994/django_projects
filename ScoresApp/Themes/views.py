from django.shortcuts import render
from .models import Lessons

# Create your views here.
def theme_lessons(request):
    value = Lessons.objects.all()
    return render(request, 'dars.html', {'value': value})