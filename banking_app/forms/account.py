from django import forms
from banking_app.models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'account_type',
            'account_pin'
        ]
