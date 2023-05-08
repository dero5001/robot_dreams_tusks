from django.forms import *
from .models import Book


class BookForm(ModelForm):
    title = CharField(max_length=100)
    autor = CharField(max_length=100)

    class Meta:
        model = Book
        fields = ('title', 'autor')
