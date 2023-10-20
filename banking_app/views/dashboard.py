from django.shortcuts import render
from banking_app.models.transaction import Transaction
from banking_app.models.account import Account


def dashboard(request):
    foundAccount = Account.objects.get(
        account_number=request.session['account_number']
    )

    foundTransactions = Transaction.objects.filter(
        account__account_number=foundAccount.account_number
    )

    balance = 0

    for transaction in foundTransactions:
        if transaction.transaction_type == 'deposit':
            balance += transaction.amount
        elif transaction.transaction_type == 'withdrawal':
            balance -= transaction.amount

    return render(
        request,
        'dashboard.html',
        {
            'account': foundAccount,
            'transactions': foundTransactions,
            'balance': balance,
            'logged_in': 'account_number' in request.session
        }
    )
