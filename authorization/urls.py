from django.urls import path

from .views import authorization_login, authorization_register


urlpatterns = [
    path('register/', authorization_register, name='register_page'),
    path('login/', authorization_login, name='login_page'),
]
