from django.urls import path
from .views import DistrictsListView, set_language

urlpatterns = [
    path("", DistrictsListView.as_view()),
    path("setLang/<str:lang>", set_language),
]
