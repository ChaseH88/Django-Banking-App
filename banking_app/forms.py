from django import forms
from .models import Account


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
    account_number = forms.IntegerField()
    account_pin = forms.IntegerField()
