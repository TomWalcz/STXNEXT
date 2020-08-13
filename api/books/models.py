from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    authors = models.CharField(max_length=100, blank=True, default='')
    publishedDate = models.PositiveIntegerField()
    # industryIdentifiers = models.CharField(max_length=100, blank=True, default='')
    # pageCount = models.PositiveIntegerField()
    # printType = models.CharField(max_length=100, blank=True, default='')