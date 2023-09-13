from django.db import models


# Create your models here.
class Capitals(models.Model):
    contry_uz = models.CharField(max_length=255)
    capital_uz = models.CharField(max_length=255)

    contry_en = models.CharField(max_length=255)
    capital_en = models.CharField(max_length=255)

    contry_ru = models.CharField(max_length=255)
    capital_ru = models.CharField(max_length=255)

    class Meta:
        db_table = "capitals"
