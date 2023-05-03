from django.urls import path
from .views import BooksList, DetailBook #CreateBook


urlpatterns = [
    path('', BooksList.as_view(), name='Books list'),
    #path('create', CreateBook, name='Create Book'),
    path('<int:pk>', DetailBook.as_view(), name='Detail Book')
]