from django.urls import path

from .views import index_page, search_page, view_page, category_page, random_recipe_from_ai

urlpatterns = [
    path('', index_page, name='index_page'),
    path('search/', search_page, name='search_page'),
    path('view/', view_page, name='view_page'),
    path('category/', category_page, name='category_page'),
    path('random_recipe', random_recipe_from_ai, name='random_recipe_from_ai')
]
