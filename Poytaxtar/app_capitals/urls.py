from django.urls import path

from .views import CapitalsListView, setLanguage

urlpatterns = [
    path("", CapitalsListView.as_view()),
    path("setLang/<str:lang>", setLanguage),
]
