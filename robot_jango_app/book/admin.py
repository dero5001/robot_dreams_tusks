from django.contrib import admin
from book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
