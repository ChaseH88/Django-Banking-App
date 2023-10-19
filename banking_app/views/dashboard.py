from django.shortcuts import render
from banking_app.models import Account


def dashboard(request):
    foundAccount = Account.objects.get(
        account_number=request.session['account_number']
    )
    return render(
        request,
        'dashboard.html',
        {
            'account': foundAccount
        }
    )
