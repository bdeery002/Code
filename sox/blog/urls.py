from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("random", views.random_page, name="random_page"),
    path("propose", views.propose_edit, name="propose_new"),
    path("propose/<str:title>", views.propose_edit, name="propose_edit"),
]