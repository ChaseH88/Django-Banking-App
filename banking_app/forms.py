from django import forms
from .models import Account, Transaction
from django.core.validators import MaxValueValidator


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'account_type',
            'account_pin'
        ]


class LoginForm(forms.Form):
    account_number = forms.IntegerField(
        min_value=10000000,
        max_value=99999999,
        label='Account Number',
    )
    account_pin = forms.IntegerField(
        min_value=1000,
        max_value=9999,
        label='Account PIN',
    )

    def clean(self):
        cleaned_data = super().clean()
        account_number = cleaned_data.get("account_number")
        account_pin = cleaned_data.get("account_pin")
        account = Account.objects.filter(account_number=account_number).first()

        # handle not found account number
        if not account:
            raise forms.ValidationError("Invalid account number.")

        # handle incorrect PIN
        if account and account.account_pin != account_pin:
            raise forms.ValidationError("Invalid account PIN.")


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'transaction_type',
            'amount'
        ]
