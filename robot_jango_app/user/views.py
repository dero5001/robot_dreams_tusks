from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .models import User
from .forms import UserForm
from .serializers import UserSerializer


class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'


class UsersList(ListView):
    model = User


class DetailUser(DetailView):
    model = User


class CreateUser(CreateView):
    model = User
    form_class = UserForm
    success_url = '/users'


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPaginator

