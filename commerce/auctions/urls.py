from django.urls import path
from . import views
app_name = "auctions"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.listing_page, name="listing_page"),
    path("create", views.create_listing, name="create_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing/<int:listing_id>/watchlist", views.toggle_watchlist, name="toggle_watchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:category_name>", views.category_listings, name="category_listings"),
    ]