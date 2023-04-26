from django.db import models
from user.models import User
from book.models import Book


class Purchase(models.Model):
    user = models.ManyToManyField(User)
    book = models.ManyToManyField(Book)
    purchase_date = models.DateField()

    class Meta:
        db_table = 'purchase'

    def __str__(self):
        return f'Purchase № {self.id} for the book {self.book.title} was done at {self.purchase_date} by {self.user.first_name}'
