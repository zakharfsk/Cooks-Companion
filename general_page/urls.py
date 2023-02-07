from django.urls import path

from .views import index_page, search_page, view_page, category_page

urlpatterns = [
    path('', index_page, name='index_page'),
    path('search/', search_page, name='search_page'),
    path('view/', view_page, name='view_page'),
    path('category/', category_page, name='category_page'),
]
