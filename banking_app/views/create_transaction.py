from django.shortcuts import render, redirect
from banking_app.models import Account
from banking_app.forms.transaction import TransactionForm


def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.account = Account.objects.get(
                account_number=request.session['account_number'])
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'create_transaction.html', {'form': form})
