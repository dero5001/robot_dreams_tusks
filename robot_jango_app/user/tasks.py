from celery import shared_task
from.models import User


@shared_task
def hello_tusk():
    print('Hello to you')


@shared_task
def purchases_count(user_id):
    user = User.objects.get(id=user_id)
    print(user.purchases.count())


@shared_task
def users_count():
    users = User.objects.all()
    print(users.count())

