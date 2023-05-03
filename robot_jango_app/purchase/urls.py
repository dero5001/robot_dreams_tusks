from django.urls import path
from .views import PurchaseList, DetailPurchase, CreatePurchase


urlpatterns = [
    path('', PurchaseList.as_view(), name='Purchase list'),
    path('create', CreatePurchase.as_view(), name='Create Purchase'),
    path('<int:pk>', DetailPurchase.as_view(), name='Detail Purchase')
]