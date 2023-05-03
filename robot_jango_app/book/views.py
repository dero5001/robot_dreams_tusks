from django.http import HttpResponse
from django.core import serializers
from book.models import Book
from django.views.generic import ListView, DetailView


class BooksList(ListView):
    model = Book


class DetailBook(DetailView):
    model = Book

