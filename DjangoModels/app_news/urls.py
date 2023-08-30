from django.urls import path
from .views import NewsListView

urlpatterns = [
    path('', NewsListView, name='news_list')
]
