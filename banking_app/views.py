from django.shortcuts import render, redirect
from .forms import AccountForm


def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AccountForm()
    return render(request, 'create_account.html', {'form': form})
