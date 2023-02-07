import time

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from .services.meal_api.meal_services import get_meal_categories, get_all_meals_by_category, get_all_meal, \
    get_meal_by_id


# Create your views here.


def index_page(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'general_page/index.html',
        {
            'user': request.user,
            'categories': get_meal_categories(),
        }
    )


def category_page(request: WSGIRequest) -> HttpResponse:
    category = request.GET.get('c', '')

    return render(
        request,
        'general_page/category.html',
        {
            'user': request.user,
            'meal_category': get_all_meals_by_category(category),
        }
    )


def search_page(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'general_page/search.html',
        {
            'user': request.user,
            'meals': get_all_meal(),
        }
    )


def view_page(request: WSGIRequest) -> HttpResponse:
    meal_id = request.GET.get('id', '')

    return render(
        request,
        'general_page/view.html',
        {
            'user': request.user,
            'meal': get_meal_by_id(meal_id),
        }
    )
