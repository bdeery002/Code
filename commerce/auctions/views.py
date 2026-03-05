from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Listing, Bid, Comment, User

def index(request):

    active_listings = Listing.objects.filter(is_active=True)
    
    return render(request, "auctions/index.html", {
        "listings": active_listings
    })

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # CHANGE THIS LINE: Point to your new User model in auctions/models.py
        from .models import User 
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
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def listing_page(request, listing_id):
    # Fetch the specific listing or return a 404 error if it's missing
    listing = Listing.objects.get(pk=listing_id)
    
    return render(request, "auctions/listing.html", {
        "listing": listing
    })
    
    
