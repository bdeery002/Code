from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing, Bid
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ListingForm, BidForm


def index(request):

    active_listings = Listing.objects.filter(is_active=True)
    
    return render(request, "auctions/index.html", {
        "listings": active_listings
    })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to home page or login page here
    else:
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("auctions:index")
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return redirect("auctions:index")


def listing_page(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    error_message = None

    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            new_bid_amount = form.cleaned_data['amount']
            
            if new_bid_amount > listing.current_price:
                bid = form.save(commit=False)
                bid.user = request.user
                bid.listing = listing
                bid.save()
                
                listing.current_price = new_bid_amount
                listing.save()
                return redirect("auctions:listing_page", listing_id=listing.id)
            else:
                error_message = "Your bid must be higher than the current price."
    
    # Always provide a blank form for the GET request
    bid_form = BidForm()
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "bid_form": bid_form,
        "error_message": error_message
    })
  
    
def create_listing(request):
    if request.method == "POST":
        # 1. Fill the form with the data from the user
        form = ListingForm(request.POST)
        
        # 2. Check if the data is valid (correct numbers, no empty titles, etc.)
        if form.is_valid():
            # 3. Create the object but don't save to DB yet (commit=False)
            # because we need to manually attach the owner (the logged-in user)
            new_listing = form.save(commit=False)
            new_listing.owner = request.user
            new_listing.save()
            return redirect("auctions:index")
    else:
        # 4. If it's a GET request, create a blank form to show the user
        form = ListingForm()

    # 5. Send that 'form' variable to the template
    return render(request, "auctions/create_listing.html", {
        "form": form
    })


@login_required(login_url="/login")
def toggle_watchlist(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if listing in request.user.watchlist.all():
        request.user.watchlist.remove(listing)
    else:
        request.user.watchlist.add(listing)
    return redirect("auctions:listing_page", listing_id=listing_id)



def watchlist(request):
    listings = request.user.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "watchlist": listings
    })

def categories(request):
    # This gets every unique category but excludes any that are null or empty
    categories_list = Listing.objects.exclude(category__isnull=True).exclude(category="").values_list('category', flat=True).distinct()
    
    return render(request, "auctions/categories.html", {
        "categories": categories_list
    })

def category_listings(request, category_name):
    # This filters listings to only show the ones in the chosen category
    listings = Listing.objects.filter(category=category_name, is_active=True)
    return render(request, "auctions/category_listings.html", {
        "category_name": category_name,
        "listings": listings
    })