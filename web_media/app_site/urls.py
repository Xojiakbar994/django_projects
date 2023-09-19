from django.urls import path
from .views import ThemesView, PlansView

urlpatterns = [
    path("plans/", PlansView.as_view(), name="plans"),
    path("", ThemesView.as_view(), name="themes"),
]
