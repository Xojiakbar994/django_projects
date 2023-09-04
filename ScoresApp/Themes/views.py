from django.shortcuts import render
from .models import Lessons

# Create your views here.
def ShowLessonsViev(request):
    context = {}
    lessons = Lessons.objects.all()
    context['lessons'] = lessons
    return render(request, 'dars.html', {context: lessons})