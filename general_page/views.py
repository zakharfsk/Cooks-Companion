from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index_page(request: WSGIRequest) -> HttpResponse:
    return render(request, 'general_page/index.html', {'user': request.user})


def search_page(request: WSGIRequest) -> HttpResponse:
    return render(request, 'general_page/search.html', {})


def view_page(request: WSGIRequest) -> HttpResponse:
    return render(request, 'general_page/view.html', {})
