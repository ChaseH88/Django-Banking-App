from django import forms
from banking_app.models.transaction import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'transaction_type',
            'amount'
        ]
