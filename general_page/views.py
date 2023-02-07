from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from .services.meal_api.meal_services import get_meal_categories


# Create your views here.


def index_page(request: WSGIRequest) -> HttpResponse:
    categories = get_meal_categories()

    return render(
        request,
        'general_page/index.html',
        {
            'user': request.user,
            'categories': categories,
        }
    )


def category_page(request: WSGIRequest) -> HttpResponse:
    category = request.GET.get('c', '')

    return render(
        request,
        'general_page/category.html',
        {
            'user': request.user,
        }
    )


def search_page(request: WSGIRequest) -> HttpResponse:
    return render(request, 'general_page/search.html', {})


def view_page(request: WSGIRequest) -> HttpResponse:
    return render(request, 'general_page/view.html', {})
