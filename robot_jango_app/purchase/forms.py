from django.forms import *
from .models import Purchase


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
