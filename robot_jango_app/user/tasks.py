from celery import shared_task
from.models import User


@shared_task
def hello_tusk():
    print('Hello to you')


@shared_task
def purchases_count(user_id):
    purchases = User.purchases.filter(id=user_id)
    print(purchases.count())


@shared_task
def users_count():
    users = User.objects.all()
    print(users)

