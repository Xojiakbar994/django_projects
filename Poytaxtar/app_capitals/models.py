from django.db import models


# Create your models here.
class Capitals(models.Model):
    country_uz = models.CharField(max_length=255)
    capital_uz = models.CharField(max_length=255)

    country_en = models.CharField(max_length=255)
    capital_en = models.CharField(max_length=255)

    country_ru = models.CharField(max_length=255)
    capital_ru = models.CharField(max_length=255)

    class Meta:
        db_table = "capitals"
