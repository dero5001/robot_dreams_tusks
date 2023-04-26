from django.http import HttpResponse
from django.core import serializers
from user.models import User


def my_view(request):
    users = User.objects.all()
    result = serializers.serialize('json', users)
    return HttpResponse(result, content_type="application/json")

