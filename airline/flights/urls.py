from xml.etree.ElementInclude import include
from django.urls import path
from . import views

app_name = "flights"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>/", views.flight_detail, name="flight_detail"),
    path("<int:flight_id>/book/", views.book_flight, name="book_flight"),
    
]