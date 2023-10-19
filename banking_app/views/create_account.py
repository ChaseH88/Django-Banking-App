from django.shortcuts import render, redirect
from banking_app.forms.account import AccountForm


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
