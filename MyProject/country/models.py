from django.db import models


# Create your models here.
class Countries(models.Model):
    name = models.CharField(max_length=100, verbose_name="Country name")
    population = models.IntegerField(verbose_name="Population")
    area = models.FloatField(verbose_name="Area")
    density = models.FloatField(verbose_name="Density")

    class Meta:
        db_table = "countries"
