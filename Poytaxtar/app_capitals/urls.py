from django.urls import path

from .views import CapitalsListView

urlpatterns = [
    path("", CapitalsListView.as_view()),
    path("setLanguage/<str:lang>", CapitalsListView.as_view()),
]
