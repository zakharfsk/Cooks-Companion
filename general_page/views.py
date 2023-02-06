from django.shortcuts import render

# Create your views here.


def index_page(request):
    return render(request, 'general_page/index.html', {})


def search_page(request):
    return render(request, 'general_page/serch.html', {})


def view_page(request):
    return render(request, 'general_page/view.html', {})
