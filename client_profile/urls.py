from django.urls import path


urlpatterns = [
    path('', lambda x: x, name='index_page'),
]
