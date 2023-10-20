from django.shortcuts import render, redirect
from banking_app.models.transaction import Transaction
from banking_app.utils.account import is_logged_in, get_account


def dashboard(request):

    if not is_logged_in(request):
        return redirect('login')

    foundAccount = get_account(request)

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
            'logged_in': is_logged_in(request),
            'welcome_message': 'Hello ' + foundAccount.first_name.capitalize() + ' ' + foundAccount.last_name.capitalize() + ', welcome to your dashboard!',
            'customer_since': 'Customer since ' + foundAccount.date.strftime('%B %Y')
        }
    )
