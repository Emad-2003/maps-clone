# map_app/views.py

from django.shortcuts import render


def home(request):
    # Get user input (latitude and longitude)
    latitude = float(request.GET.get('latitude', 0))
    longitude = float(request.GET.get('longitude', 0))

    return render(request, 'home_advanced.html', {
        'latitude': latitude,
        'longitude': longitude,
    })
