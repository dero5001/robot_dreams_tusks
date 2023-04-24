from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)

    class Meta:
        db_table = 'book'
