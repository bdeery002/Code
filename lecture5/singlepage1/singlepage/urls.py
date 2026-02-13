from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    # The <int:num> part means that Django will capture an integer from the URL and pass it as the num argument to the section view
    path("sections/<int:num>", views.section, name="section")
]