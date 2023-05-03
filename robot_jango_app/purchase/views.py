from .models import Purchase
from .forms import PurchaseForm
from django.views.generic import ListView, DetailView, CreateView


class PurchaseList(ListView):
    model = Purchase


class DetailPurchase(DetailView):
    model = Purchase


class CreatePurchase(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = '/purchases'


