from django.http import HttpResponse
from user.models import User


def my_view(request):
    return HttpResponse(User.objects.all())

