from django.shortcuts import render, get_object_or_404
from .models import SoxControl, Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

def load_workflow(request, workflow_name):
    """
    Returns just the SVG partial for the requested workflow.
    Used by HTMX when clicking the 'P2P' or 'OTC' tabs.
    """
    template = f"sox_controls/partials/workflows/{workflow_name}_workflow.html"
    return render(request, template)

def index(request):
    """
    The main dashboard. Handles both full page loads and HTMX 
    live-filtering for the control table.
    """
    # 1. Get filters from the request (search bars or SVG clicks)
    f_proc = request.GET.get('filter_proc', '')
    f_sub = request.GET.get('filter_sub', '')
    f_desc = request.GET.get('filter_desc', '')
    f_risk = request.GET.get('filter_risk', '')

    controls = SoxControl.objects.all()

    # 2. Apply filtering logic
    if f_proc:
        controls = controls.filter(process_name__icontains=f_proc)
    if f_sub:
        controls = controls.filter(sub_process__icontains=f_sub)
    if f_desc:
        controls = controls.filter(control_description__icontains=f_desc)
    if f_risk:
        controls = controls.filter(risk__icontains=f_risk)

    # 3. Paywall / Preview Logic
    # If the user is not logged in, we truncate the description to make it 'gated'
    is_paid = request.user.is_authenticated # Simplified check for your MVP
    
    if not is_paid:
        for control in controls:
            # Show only the first 10 words followed by a '...'
            words = control.control_description.split()
            if len(words) > 10:
                control.control_description = " ".join(words[:10]) + "... [Login to view full control]"

    context = {
        "controls": controls,
        "is_paid": is_paid,
        "flights": Flight.objects.all(),
        "airports": Airport.objects.all(),
    }

    # 4. HTMX response: Return ONLY the table rows if filtering
    if request.headers.get('HX-Request'):
        return render(request, "sox_controls/partials/control_table_rows.html", context)

    # 5. Standard response: Return the full page
    return render(request, "sox_controls/index.html", context)

def filter_by_process(request, process_slug):
    # Get the parent workflow from query param (e.g., ?workflow=p2p)
    workflow_slug = request.GET.get('workflow')
    
    # Filter by the parent process AND the specific sub-step (from the SVG)
    controls = SoxControl.objects.filter(
        process__slug=workflow_slug,
        sub_process__icontains=process_slug.replace('_', ' ')
    )
    
    return render(request, "sox_controls/partials/control_table_rows.html", {"controls": controls})
    
def flight_detail(request, flight_id):
    """View for the legacy Flight detail (from CS50 lectures)"""
    flight = get_object_or_404(Flight, pk=flight_id)
    passengers = flight.passengers.all()
    available_passengers = Passenger.objects.exclude(flights=flight)

    return render(request, "sox_controls/sox_controls_detail.html", {
        "flight": flight,
        "passengers": passengers,
        "available_passengers": available_passengers,
    })

def book_flight(request, flight_id):
    """Handles booking passengers onto flights"""
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)

        # Ensure the namespace matches your 'urls.py' app_name
        return HttpResponseRedirect(reverse("sox_controls:flight_detail", args=(flight.id,)))