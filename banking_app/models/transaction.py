from django.db import models
from banking_app.models.account import Account


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
    date = models.DateField(
        auto_now_add=True
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='transactions',
        to_field='account_number'
    )

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - ${self.amount} on {self.date}"
