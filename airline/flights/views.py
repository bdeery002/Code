
from django.shortcuts import render, get_object_or_404
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

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
#


def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    passengers = flight.passengers.all()
    available_passengers = Passenger.objects.exclude(flights=flight)

    return render(request, "flights/flight_detail.html", {
        "flight": flight,
        "passengers": passengers,
        "available_passengers": available_passengers,
    })





def book_flight(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)

    
        return HttpResponseRedirect(
                    reverse("flights:flight_detail", args=(flight.id,))
                )

