from django.shortcuts import redirect


def signout(request):
    request.session.flush()
    return redirect('home')
