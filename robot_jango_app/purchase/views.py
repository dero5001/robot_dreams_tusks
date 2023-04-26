from django.http import HttpResponse
from django.core import serializers
from purchase.models import Purchase


def my_view(request):
    purchases = Purchase.objects.all()
    result = serializers.serialize('json', purchases)
    return HttpResponse(result, content_type="application/json")
