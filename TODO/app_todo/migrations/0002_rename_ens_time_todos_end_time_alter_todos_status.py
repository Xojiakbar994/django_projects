# Generated by Django 4.2.5 on 2023-09-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_todo", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todos",
            old_name="ens_time",
            new_name="end_time",
        ),
        migrations.AlterField(
            model_name="todos",
            name="status",
            field=models.CharField(
                choices=[("a", "active"), ("n", "not yet"), ("d", "done")],
                max_length=15,
                verbose_name="Status",
            ),
        ),
    ]