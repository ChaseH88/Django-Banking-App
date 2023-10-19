from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Account


def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            request.session['account_number'] = account.account_number
            return redirect('dashboard')
    else:
        form = AccountForm()
    return render(request, 'create_account.html', {'form': form})


def dashboard(request):
    foundAccount = Account.objects.get(
        account_number=request.session['account_number']
    )
    return render(request, 'dashboard.html', {'account': foundAccount})
