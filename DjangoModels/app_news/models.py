from django.db import models

# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=255, verbose_name='Yangilik sarlavhasi')
    news_desc = models.CharField(max_length=255, verbose_name='Yangilik tavsifi')
    news_text = models.TextField(verbose_name='Yangilik matni')
    news_date = models.DateField(verbose_name='Joylangan sana')

    def __str__(self):
        return self.news_title
    
