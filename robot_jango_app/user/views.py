from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet
from .models import User
from .forms import UserForm
from .serializers import UserSerializer


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

