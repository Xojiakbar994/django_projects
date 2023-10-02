from django.db import models


# Create your models here.
class Pupils(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Ism")
    last_name = models.CharField(max_length=25, verbose_name="Familiya")
    exam_mark = models.IntegerField(verbose_name="Imtohon bahosi")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
