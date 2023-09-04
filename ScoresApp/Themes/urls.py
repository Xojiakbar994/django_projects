from django.urls import path
from .views import ShowLessonsViev

urlpatterns = [
    path('', ShowLessonsViev, name='themes'),
]