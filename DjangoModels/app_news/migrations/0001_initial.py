# Generated by Django 4.2.3 on 2023-08-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=255, verbose_name='Yangilik sarlavhasi')),
                ('news_desc', models.CharField(max_length=255, verbose_name='Yangilik tavsifi')),
                ('news_text', models.TextField(verbose_name='Yangilik matni')),
                ('news_date', models.DateField(verbose_name='Joylangan sana')),
            ],
        ),
    ]