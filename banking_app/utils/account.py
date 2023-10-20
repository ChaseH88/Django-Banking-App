from banking_app.models.account import Account


def is_logged_in(request):
    return 'account_number' in request.session


def get_account(request):
    if is_logged_in(request):
        return Account.objects.get(
            account_number=request.session['account_number']
        )
    else:
        return None
