from django.shortcuts import render, redirect
from banking_app.models.account import Account
from banking_app.forms.login import LoginForm
from banking_app.utils.account import is_logged_in


def login(request):

    if is_logged_in(request):
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            account_number = form.cleaned_data['account_number']
            account_pin = form.cleaned_data['account_pin']
            try:
                foundAccount = Account.objects.get(
                    account_number=account_number,
                    account_pin=account_pin
                )
                request.session['account_number'] = foundAccount.account_number
                return redirect('dashboard')
            except Account.DoesNotExist:
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
