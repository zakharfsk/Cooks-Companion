from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def client_profile(request: WSGIRequest) -> HttpResponse:
    return render(request, 'client_profile/client_profile.html', {})
