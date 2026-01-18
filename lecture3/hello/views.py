from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")

def brian(request):
    # Fixed the name here to match the function name, 
    # unless you intentionally wanted it to say Brendan!
    return HttpResponse("Hello, Brian!")

def greet(request, name): 
   return render(request, "hello/greet.html", {"name":name.capitalize()})

