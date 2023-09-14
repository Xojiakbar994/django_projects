from django.db import models


# Create your models here.
class Districts(models.Model):
    district_name_uz = models.CharField(max_length=255)
    district_name_en = models.CharField(max_length=255)
    district_name_ru = models.CharField(max_length=255)
    district_type = models.IntegerField()
    district_region_id = models.IntegerField()

    class Meta:
        db_table = "districts"
