from django.db import models
from django.core.validators import MaxValueValidator
import random


class Account(models.Model):
    """A bank account"""

    CHECKING = 'checking'
    SAVINGS = 'savings'
    ACCOUNT_TYPES = [
        (CHECKING, 'Checking'),
        (SAVINGS, 'Savings'),
    ]

    account_number = models.PositiveIntegerField(
        unique=True,
        validators=[MaxValueValidator(
            99999999
        )],
        default=random.randint(10000000, 99999999)
    )
    account_pin = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999)]
    )
    account_type = models.CharField(
        max_length=8, choices=ACCOUNT_TYPES, default=CHECKING
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return {
            'account_number': self.account_number,
            'account_pin': self.account_pin,
            'account_type': self.account_type,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date': self.date,
        }
