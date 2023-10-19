from django.shortcuts import render, redirect
from .forms import AccountForm, LoginForm, TransactionForm
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


def login(request):
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


def signout(request):
    request.session.flush()
    return redirect('home')


def home(request):
    if request.session.get('account_number'):
        return redirect('dashboard')
    else:
        return redirect('login')


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
