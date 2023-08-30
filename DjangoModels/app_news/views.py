from django.shortcuts import render

from .models import News

# Create your views here.
def NewsListView(request):
    context = {}
    context['data'] = News.objects.all()
    return render(request, 'news_list.html', context)