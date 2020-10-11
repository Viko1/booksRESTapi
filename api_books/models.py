from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    published_date = models.CharField(max_length=20)
    language = models.CharField(max_length=300)
    number_isbm = models.IntegerField(default='0')
    page_count = models.IntegerField(default='0')
    thumbnail = models.URLField(max_length=200)

    def __str__(self):
        return self.title