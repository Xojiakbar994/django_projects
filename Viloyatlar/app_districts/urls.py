from django.urls import path
from .views import DistrictsListView, setLanguage

urlpatterns = [
    path("", DistrictsListView.as_view()),
    path("setLang/<str:lang>", setLanguage),
]
