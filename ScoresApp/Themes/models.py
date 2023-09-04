from django.db import models

# Create your models here.
class Lessons(models.Model):
    lesson_title = models.CharField(max_length=255, verbose_name='Lesson title')

    def __str__(self):
        return self.lesson_title