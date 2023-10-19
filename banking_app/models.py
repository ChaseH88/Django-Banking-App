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

    # this needs to be random numbers of 8 digits
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
    # balance should start as 0 but still be a decimal
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.account_number}"


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
