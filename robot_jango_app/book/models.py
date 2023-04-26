from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f'Book with ID {self.id} has title: {self.title}, was written by: {self.autor}'
