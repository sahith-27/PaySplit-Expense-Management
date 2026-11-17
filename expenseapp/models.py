from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField()

    # True if the expense is shared
    is_shared = models.BooleanField(default=False)

    # Number of people sharing the expense
    shared_people = models.IntegerField(default=1)

    def __str__(self):
        return self.title