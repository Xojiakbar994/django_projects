# Generated by Django 4.2.5 on 2023-09-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pupils",
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
                ("first_name", models.CharField(max_length=25, verbose_name="Ism")),
                ("last_name", models.CharField(max_length=25, verbose_name="Familiya")),
                ("exam_mark", models.IntegerField(verbose_name="Imtohon bahosi")),
            ],
        ),
    ]
