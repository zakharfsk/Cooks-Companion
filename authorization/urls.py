from django.urls import path

from .views import client_profile


urlpatterns = [
    path('', client_profile, name='index_page'),
]
