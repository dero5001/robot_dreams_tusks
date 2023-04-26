from django.http import HttpResponse
from django.core import serializers
from book.models import Book


def my_view(request):
    books = Book.objects.all()
    result = serializers.serialize('json', books)
    return HttpResponse(result, content_type="application/json")
