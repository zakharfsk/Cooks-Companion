from django.http.response import HttpResponse

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.


def authorization_login(request: WSGIRequest) -> HttpResponse:
    return render(request, 'authorization/login.html', {})


def authorization_register(request: WSGIRequest) -> HttpResponse:
    return render(request, 'authorization/register.html', {})
