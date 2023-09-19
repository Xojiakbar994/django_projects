from django.db import models


# Create your models here.
class Themes(models.Model):
    theme = models.CharField(max_length=255, verbose_name="themes")

    class Meta:
        db_table = "themes"


class Plans(models.Model):
    plan = models.CharField(max_length=255, verbose_name="plan")
    plan_text = models.TextField(verbose_name="plan_text")
    plan_theme = models.ForeignKey(
        Themes, on_delete=models.CASCADE, verbose_name="plan_theme"
    )

    class Meta:
        db_table = "plans"
