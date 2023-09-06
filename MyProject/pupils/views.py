from django.shortcuts import render
from .models import Student
from django.views.generic import ListView

# Create your views here.
class StudentListView(ListView):
    def get(self, request):
        students = Student.objects.all()
        score = Student.objects.all()
        month = Student.objects.all()
        return render(request, 'student_list.html', {'add': students, 'score': score, 'month': month})