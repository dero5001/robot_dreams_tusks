from django.views.generic import ListView, DetailView, CreateView
from .models import User
from .forms import UserForm


class UsersList(ListView):
    model = User


class DetailUser(DetailView):
    model = User


class CreateUser(CreateView):
    model = User
    form_class = UserForm
    success_url = '/users'

