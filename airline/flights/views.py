
from django.shortcuts import render
from .models import Flight, Airport

def index(request):
    """Display all flights"""
    flights = Flight.objects.all()
    airports = Airport.objects.all()
    return render(request, "flights/index.html", 
                  # Pass flights and airports to the template
                  {
        "flights": flights,
        "airports": airports
    })  