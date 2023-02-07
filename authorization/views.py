from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def authorization_login(request: WSGIRequest) -> HttpResponse:

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authorization/login.html', {'error': 'Invalid credentials'})

    else:
        return render(request, 'authorization/login.html', {})


def authorization_register(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index_page')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request, 'authorization/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'authorization/register.html', {'form': form})


@login_required(login_url='login/')
def authorization_logout(request: WSGIRequest) -> HttpResponse:
    logout(request)
    return redirect('index_page')
