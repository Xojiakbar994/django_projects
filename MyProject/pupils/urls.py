from django.urls import path
from .views import StudentListView

urlpatterns = [
    path('score/', StudentListView.as_view(), name='student_list')
]