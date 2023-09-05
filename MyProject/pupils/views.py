from django.shortcuts import render
from .models import Student
from django.views.generic import ListView

# Create your views here.
class StudentListView(ListView):
    def get(self, request, month):
        students = Student.objects.all()
        month = Student.objects.filter(month=month)
        return render(request, 'student_list.html', {'add': students, 'month': month})