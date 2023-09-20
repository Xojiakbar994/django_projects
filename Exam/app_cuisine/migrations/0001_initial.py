# Generated by Django 4.2.5 on 2023-09-20 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Foods",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("food_uz", models.CharField(max_length=100, verbose_name="food_uz")),
                ("food_en", models.CharField(max_length=100, verbose_name="food_en")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author",
                    ),
                ),
            ],
            options={
                "db_table": "foods",
            },
        ),
        migrations.CreateModel(
            name="Recipes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("recipe_uz", models.TextField(verbose_name="recipe_uz")),
                ("recipe_en", models.TextField(verbose_name="recipe_en")),
                (
                    "recipe_food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_cuisine.foods",
                        verbose_name="recipe_food",
                    ),
                ),
            ],
            options={
                "db_table": "recipe",
            },
        ),
    ]
