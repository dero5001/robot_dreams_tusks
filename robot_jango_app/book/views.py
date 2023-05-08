from .models import Book
from django.views.generic import ListView, DetailView, CreateView
from .forms import BookForm


class BooksList(ListView):
    model = Book


class DetailBook(DetailView):
    model = Book


class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    success_url = '/books'
