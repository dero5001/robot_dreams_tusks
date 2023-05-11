from django.forms import *
from .models import User


class UserForm(ModelForm):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    age = CharField(max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'age')
