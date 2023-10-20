from django.shortcuts import render, redirect
from banking_app.models.transaction import Transaction
from banking_app.models.account import Account
from banking_app.forms.transaction import TransactionForm
from banking_app.utils.account import is_logged_in, get_account


def create_transaction(request):

    if not is_logged_in(request):
        return redirect('login')

    foundAccount = get_account(request)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.account = foundAccount
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
                        {
                            'form': form,
                            'error': 'Insufficient funds',
                            'is_logged_in': is_logged_in(request),
                        }
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
            'logged_in': is_logged_in(request)
        }
    )
