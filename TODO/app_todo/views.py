from django.shortcuts import render
from django.views.generic import ListView

from .models import Todos


# Create your views here.
class TodoListView(ListView):
    model = Todos
    template_name = ""

    def get_queryset(self):
        fk = self.kwargs["fk"]
        try:
            queryset = Todos.objects.filter("fk")
        except:
            queryset = Todos.objects.all()

        return queryset
