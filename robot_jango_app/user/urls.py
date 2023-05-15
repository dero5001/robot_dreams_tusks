from django.urls import path
from .views import UsersList, DetailUser, CreateUser, UserViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('', UsersList.as_view(), name='Users list'),
    path('create', CreateUser.as_view(), name='Create User'),
    path('<int:pk>', DetailUser.as_view(), name='Detail User')
]

router = SimpleRouter()
router.register('router', UserViewSet)

urlpatterns += router.urls
