from .models import Book
from .forms import BookForm
from .serializers import BookSerializer
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet


class BooksList(ListView):
    model = Book


class DetailBook(DetailView):
    model = Book


class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    success_url = '/books'


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
