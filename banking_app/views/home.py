from django.shortcuts import redirect


def home(request):
    if request.session.get('account_number'):
        return redirect('dashboard')
    else:
        return redirect('login')
