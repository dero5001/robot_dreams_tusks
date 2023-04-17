from django.http import HttpResponse


def user_view(request):
    return HttpResponse('Hello, Users!')
