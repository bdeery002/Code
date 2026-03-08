from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Listing, Bid, Comment, User
from django.contrib.auth.decorators import login_required

def index(request):

    active_listings = Listing.objects.filter(is_active=True)
    
    return render(request, "auctions/index.html", {
        "listings": active_listings
    })

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['email'].help_text = "Optional: Used for account recovery."

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("auctions:login")   
    else: 
        form = UserRegisterForm()
    return render(request, "auctions/register.html", {
        "form": form
    })


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
    # Fetch the specific listing or return a 404 error if it's missing
    listing = get_object_or_404(Listing, pk=listing_id)
    
    return render(request, "auctions/listing.html", {
        "listing": listing
    })
    
def create_listing(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        starting_bid = request.POST.get("starting_bid")
        image_url = request.POST.get("image_url")

        new_listing = Listing(
            title=title,
            description=description,
            starting_bid=starting_bid,
            image_url=image_url,
            owner=request.user
        )
        new_listing.save()
        return redirect("auctions:index")
    return render(request, "auctions/create_listing.html")


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
