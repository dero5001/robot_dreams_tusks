from .models import Purchase
from .forms import PurchaseForm
from .serializers import PurchaseSerializer
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet


class PurchaseList(ListView):
    model = Purchase


class DetailPurchase(DetailView):
    model = Purchase


class CreatePurchase(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = '/purchases'


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
