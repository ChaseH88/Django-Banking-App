from django.shortcuts import render, redirect
from banking_app.models import Account, Transaction
from banking_app.forms.transaction import TransactionForm


def create_transaction(request):
    foundAccount = Account.objects.get(
        account_number=request.session['account_number']
    )
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.account = Account.objects.get(
                account_number=request.session['account_number']
            )
            if new_transaction.transaction_type == 'withdrawal':

                foundTransactions = Transaction.objects.filter(
                    account__account_number=foundAccount.account_number
                )

                balance = 0

                for transaction in foundTransactions:
                    if transaction.transaction_type == 'deposit':
                        balance += transaction.amount
                    elif transaction.transaction_type == 'withdrawal':
                        balance -= transaction.amount

                if balance - new_transaction.amount < 0:
                    return render(
                        request,
                        'create_transaction.html',
                        {'form': form, 'error': 'Insufficient funds'}
                    )

            new_transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()

    return render(
        request,
        'create_transaction.html',
        {
            'form': form,
            'account': foundAccount,
        }
    )
