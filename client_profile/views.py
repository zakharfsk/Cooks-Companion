from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


@login_required(login_url='login/')
def client_profile(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'client_profile/client_profile.html',
        {
            'user': request.user
        }
    )
