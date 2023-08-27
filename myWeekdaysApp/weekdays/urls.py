from django.urls import path
from .views import WeekdaysEn, WeekdaysUz, WeekdaysRu

urlpatterns = [
    path ('/en', WeekdaysEn, name='weekdays/en'),
    path ('/uz', WeekdaysUz, name='weekdays/uz'),
    path ('/ru', WeekdaysRu, name='weekdays/ru')
]