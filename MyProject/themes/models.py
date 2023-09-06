from django.db import models

# Create your models here.
class Subjects(models.Model):
    subject_name = models.CharField(max_length=50, verbose_name='Subject')

    def __str__(self):
        return self.subject_name


class Teachers(models.Model):
    teacher_fio = models.CharField(max_length=50, verbose_name='Teacher Fio')

    def __str__(self):
        return self.teacher_fio


class Lessons(models.Model):
    lesson_title = models.CharField(max_length=100, verbose_name='Lesson title')
    lesson_subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Subject ID', null=True)
    lesson_teacher = models.ManyToManyField(Teachers, verbose_name='Teachers ID', null=True)
    lesson_date = models.DateField(verbose_name='Lesson date', auto_now_add=True, null=True)
    
    def __str__(self):
        return self.lesson_title, self.lesson_subject, self.lesson_teacher, self.lesson_date
    
    def get(self):
        return Lessons.objects.all()