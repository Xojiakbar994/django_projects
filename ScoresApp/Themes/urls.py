from django.urls import path
from .views import theme_lessons

urlpatterns = [
    path('themes/', theme_lessons, name='darslar'),
]