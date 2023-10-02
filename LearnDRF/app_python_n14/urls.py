from django.urls import path
from .views import PupilsView, PupilsListView


urlpatterns = [path("", PupilsListView.as_view())]
