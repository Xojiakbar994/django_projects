from django.urls import path
from .views import WeekdaysEn
from .views import WeekdaysUz
from .views import WeekdaysRu


urlpatterns = [
    path ('/en', WeekdaysEn, name='weekdays/en'),
    path ('/uz', WeekdaysUz, name='weekdays/uz'),
    path ('/ru', WeekdaysRu, name='weekdays/ru')
]