from rest_framework import serializers
from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


purchase = Purchase.objects.all()
serialized_purchase = PurchaseSerializer(purchase)

