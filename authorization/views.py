from django.shortcuts import render

# Create your views here.


def authorization_login(request):
    return render(request, 'authorization/login.html', {})


def authorization_register(request):
    return render(request, 'authorization/register.html', {})
