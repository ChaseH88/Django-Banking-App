from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
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

    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return {
            'account_number': self.account_number,
            'account_pin': self.account_pin,
            'account_type': self.account_type,
            'balance': self.balance,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


class Transaction(models.Model):
    """A transaction for an account"""

    DEPOSIT = 'deposit'
    WITHDRAWAL = 'withdrawal'
    TRANSACTION_TYPES = [
        (DEPOSIT, 'Deposit'),
        (WITHDRAWAL, 'Withdrawal'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES,
        default=DEPOSIT)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    date = models.DateField()
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='transactions',
        to_field='account_number'
    )

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - ${self.amount} on {self.date}"
