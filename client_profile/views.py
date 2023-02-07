from django.shortcuts import render


def client_profile(request):
    return render(request, 'client_profile/client_profile.html', {})
