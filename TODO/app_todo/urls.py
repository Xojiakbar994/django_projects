from django.urls import path
from .views import TodoListView

urlpatterns = [
    path("users/<int:fk>", TodoListView.as_view()),
]
