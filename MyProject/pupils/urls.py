from django.urls import path
from .views import StudentListView

urlpatterns = [
    path('<str:month>/', StudentListView.as_view(), name='student_list')
]