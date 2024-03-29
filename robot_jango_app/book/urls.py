from django.urls import path
from .views import BooksList, DetailBook, CreateBook, BookViewSet
from rest_framework.routers import SimpleRouter


urlpatterns = [
    path('', BooksList.as_view(), name='Books list'),
    path('create', CreateBook.as_view(), name='Create Book'),
    path('<int:pk>', DetailBook.as_view(), name='Detail Book')
]

router = SimpleRouter()
router.register('router', BookViewSet)

urlpatterns += router.urls
