from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'User with ID: {self.id} is {self.first_name} {self.last_name}, has {self.age} years'
